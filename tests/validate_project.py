from pathlib import Path
import csv, json, re, subprocess, sys
from openpyxl import load_workbook
ROOT=Path(__file__).resolve().parents[1]
errors=[]; checks=[]
def ok(name,cond,detail=''):
    checks.append((name,bool(cond),detail))
    if not cond: errors.append(name)
# dataset
with (ROOT/'data/sales_data.csv').open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
ids=[r['Order_ID'] for r in rows]
required={'Order_ID','Order_Date','Customer_ID','Region','Product','Category','Quantity','Unit_Price_INR','Discount_Rate','Revenue_INR','Profit_INR','Sales_Channel','Payment_Method','Order_Status'}
ok('CSV has rows and required columns',len(rows)>0 and required.issubset(rows[0]),f'{len(rows)} rows')
ok('Order IDs unique',len(ids)==len(set(ids)),f'{len(set(ids))} unique IDs')
statuses={s:sum(r['Order_Status']==s for r in rows) for s in set(r['Order_Status'] for r in rows)}
ok('Order statuses reconcile',sum(statuses.values())==len(rows),str(statuses))
# HTML
html=(ROOT/'Interactive_Dashboard.html').read_text(encoding='utf-8')
for ident in ['region','category','channel','status','month','weekday','reset','daily','weekdays','monthly','regions','categories','statuses','products','tbody']:
    ok(f'HTML element #{ident}',f'id="{ident}"' in html)
match=re.search(r'const DATA\s*=\s*(\[.*?\]);\s*const fmt',html,re.S)
if not match:
    match=re.search(r'const DATA\s*=\s*(\[.*?\]);',html,re.S)
try:
    embedded=json.loads(match.group(1)) if match else None
except Exception as e: embedded=None
ok('Dashboard embeds valid JSON data',embedded is not None)
ok('Dashboard data row count matches CSV',embedded is not None and len(embedded)==len(rows),f'embedded={len(embedded) if embedded is not None else "invalid"}, csv={len(rows)}')
ok('Root and outputs dashboard copies match',(ROOT/'outputs/Interactive_Dashboard.html').read_bytes()==(ROOT/'Interactive_Dashboard.html').read_bytes())
# Python syntax and execution
py=ROOT/'python/ecommerce_analysis.py'
r=subprocess.run([sys.executable,str(py)],capture_output=True,text=True)
ok('Python analysis executes',r.returncode==0,(r.stdout+r.stderr)[-500:])
# Excel
try:
 wb=load_workbook(ROOT/'excel/Ecommerce_Sales_Analytics_Dashboard.xlsx',read_only=False,data_only=False)
 ok('Excel workbook has 12 expected sheets',len(wb.sheetnames)==12,str(wb.sheetnames))
 ok('Excel Sales_Data row count matches CSV',wb['Sales_Data'].max_row==len(rows)+1,f'{wb["Sales_Data"].max_row} rows incl header')
 ok('Excel charts sheet contains charts',len(wb['Charts']._charts)>=1,f'{len(wb["Charts"]._charts)} charts')
except Exception as e: ok('Excel workbook opens',False,str(e))
# notebook
try:
 nb=json.loads((ROOT/'notebooks/ecommerce_sales_analysis.ipynb').read_text())
 ok('Notebook JSON valid',isinstance(nb.get('cells'),list) and len(nb['cells'])>0,f'{len(nb.get("cells",[]))} cells')
except Exception as e: ok('Notebook JSON valid',False,str(e))
# referenced images
for m in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',(ROOT/'README.md').read_text()):
    ok(f'Readme image exists: {m}',(ROOT/m).exists())
# required docs
for p in ['sql/ecommerce_sales_analysis.sql','power_bi/DAX_Measures.txt','power_bi/Dashboard_Guide.md','docs/Data_Dictionary.md','docs/Dashboard_Report.pdf','screenshots/01_dashboard_overview.png']:
    ok(f'Required deliverable exists: {p}',(ROOT/p).is_file())
print('\n'.join(('PASS' if p else 'FAIL')+' | '+n+((' — '+d) if d else '') for n,p,d in checks))
print(f'\nRESULT: {sum(p for _,p,_ in checks)}/{len(checks)} checks passed')
sys.exit(1 if errors else 0)

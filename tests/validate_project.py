from pathlib import Path
import csv, json, re, subprocess, sys
from openpyxl import load_workbook
ROOT = Path(__file__).resolve().parents[1]
errors, checks = [], []

def ok(name, condition, detail=''):
    checks.append((name, bool(condition), detail))
    if not condition:
        errors.append(name)

# Dataset
with (ROOT / 'data/sales_data.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
ids = [r['Order_ID'] for r in rows]
required = {'Order_ID','Order_Date','Customer_ID','Region','Product','Category','Quantity','Unit_Price_INR','Discount_Rate','Revenue_INR','Profit_INR','Sales_Channel','Payment_Method','Order_Status'}
ok('CSV has 600 rows and required columns', len(rows) == 600 and required.issubset(rows[0]), f'{len(rows)} rows')
ok('Order IDs unique', len(ids) == len(set(ids)), f'{len(set(ids))} unique IDs')
statuses = {s: sum(r['Order_Status'] == s for r in rows) for s in {r['Order_Status'] for r in rows}}
ok('Order statuses reconcile', statuses == {'Delivered':387, 'Returned':99, 'Cancelled':114}, str(statuses))

# Interactive HTML dashboard
html = (ROOT / 'Interactive_Dashboard.html').read_text(encoding='utf-8')
for ident in ['region','category','channel','status','month','weekday','reset','daily','weekdays','monthly','regions','categories','statuses','products','tbody']:
    ok(f'HTML element #{ident}', f'id="{ident}"' in html)
match = re.search(r'const DATA\s*=\s*(\[.*?\]);\s*const fmt', html, re.S)
if not match:
    match = re.search(r'const DATA\s*=\s*(\[.*?\]);', html, re.S)
try:
    embedded = json.loads(match.group(1)) if match else None
except Exception:
    embedded = None
ok('Dashboard embeds valid JSON data', embedded is not None)
ok('Dashboard data matches CSV row count', embedded is not None and len(embedded) == len(rows), f'embedded={len(embedded) if embedded is not None else "invalid"}, csv={len(rows)}')
ok('Root and outputs dashboard copies match', (ROOT/'outputs/Interactive_Dashboard.html').read_bytes() == (ROOT/'Interactive_Dashboard.html').read_bytes())

# Python script syntax/execution
py = ROOT / 'python/ecommerce_analysis.py'
r = subprocess.run([sys.executable, str(py)], capture_output=True, text=True)
ok('Python analysis executes', r.returncode == 0, (r.stdout + r.stderr)[-400:])

# Excel dashboard
try:
    wb = load_workbook(ROOT/'excel/Ecommerce_Sales_Analytics_Dashboard.xlsx', data_only=False)
    expected_sheets = ['Dashboard','Insights','Sales_Data','Calc','About']
    ok('Excel has the five expected sheets', wb.sheetnames == expected_sheets, str(wb.sheetnames))
    dash = wb['Dashboard']
    ok('Excel dashboard has six native charts', len(dash._charts) == 6, f'{len(dash._charts)} charts')
    ok('Excel dashboard has four dropdown filters', len(dash.data_validations.dataValidation) == 4, f'{len(dash.data_validations.dataValidation)} validations')
    ok('Excel source rows match CSV', wb['Sales_Data'].max_row == len(rows)+1, f'{wb["Sales_Data"].max_row} rows incl header')
    wbv = load_workbook(ROOT/'excel/Ecommerce_Sales_Analytics_Dashboard.xlsx', data_only=True)
    vals = wbv['Dashboard']
    kpis = [vals['B10'].value, vals['F10'].value, vals['J10'].value, vals['N10'].value, vals['R10'].value, vals['V10'].value]
    expected = [600, 36.0768418, 4.2149553, 9322.18134366925, .165, .19]
    ok('Excel saved KPI values match source dataset', all(isinstance(a,(int,float)) and abs(a-b)<1e-6 for a,b in zip(kpis,expected)), str(kpis))
except Exception as e:
    ok('Excel workbook opens and validates', False, str(e))

# Notebook
try:
    nb = json.loads((ROOT/'notebooks/ecommerce_sales_analysis.ipynb').read_text(encoding='utf-8'))
    ok('Notebook JSON valid', isinstance(nb.get('cells'), list) and len(nb.get('cells', [])) > 0, f'{len(nb.get("cells", []))} cells')
except Exception as e:
    ok('Notebook JSON valid', False, str(e))

# README image
for img in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', (ROOT/'README.md').read_text(encoding='utf-8')):
    ok(f'Readme image exists: {img}', (ROOT/img).exists())

# Required deliverables
required_files = [
    'dashboard.png', 'excel/Ecommerce_Sales_Analytics_Dashboard.xlsx',
    'sql/ecommerce_sales_analysis.sql', 'sql/ecommerce_sales_analysis_sqlite.sql',
    'power_bi/DAX_Measures.txt', 'power_bi/Dashboard_Guide.md',
    'docs/Data_Dictionary.md', 'docs/Dashboard_Report.pdf',
    'docs/SETUP_GUIDE.md', 'docs/FINAL_AUDIT_REPORT.md',
    'python/ecommerce_analysis.py', 'notebooks/ecommerce_sales_analysis.ipynb',
    'index.html', 'tests/run_sqlite_validation.py'
]
for p in required_files:
    ok(f'Required deliverable exists: {p}', (ROOT/p).is_file())

print('\n'.join(('PASS' if passed else 'FAIL') + ' | ' + name + ((' — ' + detail) if detail else '') for name,passed,detail in checks))
print(f'\nRESULT: {sum(p for _,p,_ in checks)}/{len(checks)} checks passed')
sys.exit(1 if errors else 0)

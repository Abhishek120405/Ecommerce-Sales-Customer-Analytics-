"""Execute all SQLite-compatible portfolio queries against the included CSV."""
from pathlib import Path
import sqlite3
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / 'data' / 'sales_data.csv')
con = sqlite3.connect(':memory:')
df.to_sql('sales_data', con, index=False, if_exists='replace')
sql = (ROOT / 'sql' / 'ecommerce_sales_analysis_sqlite.sql').read_text(encoding='utf-8')
# Split on semicolons; comments are harmless to SQLite when leading a statement.
sql = '\n'.join(line for line in sql.splitlines() if not line.lstrip().startswith('--'))
statements = [s.strip() for s in sql.split(';') if s.strip()]
results = []
for i, statement in enumerate(statements, 1):
    cur = con.execute(statement)
    rows = cur.fetchall()
    results.append((i, len(rows)))
    print(f'PASS | SQLite query {i} executed | {len(rows)} result rows')
assert len(results) == 10, f'Expected 10 queries, got {len(results)}'
quality = con.execute('SELECT COUNT(*), COUNT(DISTINCT Order_ID), SUM(CASE WHEN Order_Status="Delivered" THEN 1 ELSE 0 END) FROM sales_data').fetchone()
assert quality[0] == 600 and quality[1] == 600
print(f'PASS | Dataset reconciliation | rows={quality[0]}, unique_orders={quality[1]}')
con.close()

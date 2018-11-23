from SqlExcel import SqlExcel
nw = SqlExcel('DB2T', 'bc9029', 'pwd')
cn = nw.db_connect()
sql = 'select current date from sysibm.sysdummy1'
print nw.sql_to_df(cn, sql).head()
# nw.sql_to_xl(cn, sql, r"C:")
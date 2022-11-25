import pandas as pd
filePath="副本用户明细.xlsx"
df = pd.read_excel(filePath,sheet_name="需摸排用户明细")
print(df,"\n")
df = pd.read_excel(filePath,sheet_name="需摸排用户明细",index_col= 0 ,header = 0)
print(df,"\n")

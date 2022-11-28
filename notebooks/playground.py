import pandas as pd
df = pd.read_excel(io="/Users/jakob/PycharmProjects/H2_pathways_repo/data/raw/LCOE_opt.xlsx", sheet_name='LCOE')

print(df.head())


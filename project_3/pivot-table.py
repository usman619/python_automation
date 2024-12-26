import pandas as pd

df = pd.read_excel('../assets/datasets/supermarket_sales.xlsx')

# print(df.columns)

df = df[['Gender', 'Product line', 'Total']]

pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

pivot_table.to_excel('pivot_table.xlsx', sheet_name='Report', startrow=4)
import pandas as pd
import sqlite3 as sql

conn = sql.connect('Sales.db')

cursor = conn.cursor()

# List of CSV files and corresponding table names
csv_to_table = {
    'DB/brands.csv': 'Brands',
    'DB/categories.csv': 'Categories',
    'DB/customers.csv': 'Customers',
    'DB/order_items.csv': 'OrderItems',
    'DB/orders.csv': 'Orders',
    'DB/products.csv': 'Products',
    'DB/stocks.csv': 'Stocks',
    'DB/stores.csv': 'Stores',
    'DB/staffs.csv': 'Staffs'
}

# Loop through and insert data
for csv_file, table_name in csv_to_table.items():
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    print(f"Inserted data from {csv_file} into {table_name}")

# Close the connection
conn.close()

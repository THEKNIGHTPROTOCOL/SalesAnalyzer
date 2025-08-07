import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to DB
conn = sqlite3.connect('sales.db')

# Total Sales Per Product
query1 = '''
SELECT product, SUM(quantity * price) as total_sales
FROM sales
GROUP BY product
'''

df1 = pd.read_sql_query(query1, conn)
print("Total Sales by Product:")
print(df1)

# Sales Trend Over Time
query2 = '''
SELECT date, SUM(quantity * price) as daily_total
FROM sales
GROUP BY date
'''

df2 = pd.read_sql_query(query2, conn)
print("\nSales by Date:")
print(df2)

# 📊 Plotting
plt.figure(figsize=(10, 5))
plt.bar(df1['product'], df1['total_sales'])
plt.title("Total Sales per Product")
plt.ylabel("Revenue (₹)")
plt.show()

plt.plot(df2['date'], df2['daily_total'], marker='o')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue (₹)")
plt.grid(True)
plt.show()

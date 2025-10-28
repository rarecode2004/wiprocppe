import pandas as pd
import mysql.connector
import numpy as np
df = pd.read_csv('stock.csv')

# Connect to local MariaDB/MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='Gopika',
    password='Gopi0987',
    database='ecommerce'
)

cursor = conn.cursor()
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (%s, %s, %s, %s)",
        (row['name'], row['category'], row['price'], row['stock'])
    )

conn.commit()
print("Data uploaded successfully!")

cursor.close()
conn.close()

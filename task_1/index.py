from flask import Flask, jsonify
import mysql.connector
import pandas as pd
import random

app = Flask(__name__)

# Database connection function
def get_products():
    conn = mysql.connector.connect(
        host='localhost',
        user='Gopika',
        password='Gopi0987',
        database='ecommerce'
    )
    df = pd.read_sql("SELECT * FROM products", conn)
    conn.close()
    return df

@app.route('/')
def home():
    df = get_products()
    
    # Convert first 5 products to dictionary
    products_list = df.head(5).to_dict(orient='records')
    
    # Add AI-driven stock prediction
    for product in products_list:
        # Simulate AI prediction for stock load
        product['predicted_stock_load'] = random.choice(["Low", "Medium", "High"])
    
    return jsonify({
        "message": "E-Commerce Website - AI Stock Prediction Active",
        "products": products_list
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

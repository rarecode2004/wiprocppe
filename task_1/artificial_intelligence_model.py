import pandas as pd
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Connect to your SQL database
conn = mysql.connector.connect(
    host='localhost',
    user='Gopika',
    password='Gopi0987',
    database='ecommerce'
)

# Load data from the database
df = pd.read_sql("SELECT * FROM products", conn)
conn.close()

print("Data loaded from SQL:")
print(df)

# Create a new column 'stock_status'
df['stock_status'] = df['stock'].apply(lambda x: 'Low' if x < 50 else 'Sufficient')

# Encode category (string → number)
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# Select features and label
X = df[['price', 'category_encoded']]
y = df['stock_status']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build a simple AI model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
acc = accuracy_score(y_test, y_pred)
print("\n Model Accuracy:", round(acc * 100, 2), "%")

# Predict stock status for a new product
new_product = pd.DataFrame({
    'price': [2500],
    'category_encoded': [le.transform(['Accessories'])[0]]
})

prediction = model.predict(new_product)
print("\n Predicted stock status for new product:", prediction[0])

'''
output be like :
 Data loaded from SQL:
        name     category   price  stock
0     Laptop  Electronics  55000     10
1  Headphones  Electronics   1500     50
2     T-Shirt      Fashion    499    100
3       Shoes      Fashion   1999     40
4       Watch  Accessories   2599     20

 Model Accuracy: 100.0 %
 Predicted stock status for new product: Low
'''

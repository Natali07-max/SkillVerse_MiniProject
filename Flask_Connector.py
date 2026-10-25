from flask import Flask
import mysql.connector

app = Flask(__name__)

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = db.cursor()

@app.route('/')
def home():
    return "Database connected successfully!"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# database connection
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "app_db"

def connect_to_db():
    connect = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )

    return connect

@app.route('/')
def home():
    connect = connect_to_db()
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(255))")
    cursor.execute("INSERT INTO messages (text) VALUES ('Hello from Local MySQL!')")

    connect.commit()

    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()

    cursor.close()
    connect.close()

    return jsonify({"messages": messages})

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port = 5000, debug = True)

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

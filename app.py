
from flask import Flask, render_template
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv('database.env')
DATABASE_URL = os.getenv('DATABASE_URL')

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route("/")
def hello_world():
    connection_status = "Not Connected"
    db_version = None
    # Test database connection
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        connection_status = "Connected"
        print(f"Database connected successfully: {db_version}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Database connection failed: {e}")
    
    return render_template("home.html", db_status=connection_status, db_version=db_version)

@app.route("/intake")
def intake():
    return render_template("intake.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

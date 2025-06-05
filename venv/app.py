import requests
from flask import send_file
import csv
from flask import Flask, request, render_template
from datetime import datetime
import os
from flask import current_app
import sqlite3
# ✅ Flask app setup
app = Flask(__name__)

# ✅ Logging function
def write_to_google_sheet(timestamp, name):
    url = "*********************************"
    data = {
        "sheet1": {
            "timestamp": str(timestamp),
            "name": name
        }
    }
    response = requests.post(url, json=data)
    print(response.status_code, response.text)
from flask import send_file
import csv
def init_db():
        conn = sqlite3.connect("submissions.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                name TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
init_db()  # Initialize the database at startup
# ✅ Save data to SQLite
def save_submission(timestamp, name):
    conn = sqlite3.connect("submissions.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO submissions (timestamp, name) VALUES (?, ?)", (str(timestamp), name))
    conn.commit()
    conn.close()
# ✅ Route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("username")
        timestamp = datetime.now()
        with open("submissions.txt", "a") as file:
            file.write(f"{timestamp}  {name}\n")
        write_to_google_sheet(timestamp, name)
        save_submission(timestamp, name)
        return f"<h2>Hello, {name}!</h2><p><a href='/'>Go Back</a></p>"

    # Read all submissions from the database
    conn = sqlite3.connect("submissions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, name FROM submissions ORDER BY id DESC")
    submissions = cursor.fetchall()
    conn.close()

    return render_template("form1.html", submissions=submissions)

@app.route("/download")
def download_csv():
    csv_filename = "submissions.csv"
    csv_path = os.path.join(current_app.root_path, csv_filename)
    # Read from the database instead of the text file
    conn = sqlite3.connect("submissions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, name FROM submissions ORDER BY id DESC")
    submissions = cursor.fetchall()
    conn.close()
    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Timestamp", "Name"])  # header
        for row in submissions:
            writer.writerow(row)
    return send_file(csv_path, as_attachment=True)
@app.route("/admin")
def admin():
    conn = sqlite3.connect("submissions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, name FROM submissions ORDER BY id DESC")
    submissions = cursor.fetchall()
    conn.close()
    return render_template("admin.html", submissions=submissions)

if __name__ == "__main__":
    app.run(debug=True)



    

# Call it once at startup

# ✅ Database function

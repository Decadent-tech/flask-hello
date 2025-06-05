# Flask Hello App 🙌

A simple Flask-based web app that allows users to submit their name through a form.
The app stores submissions in a local SQLite database, displays recent submissions on the homepage, 
and allows an admin to download the data as a CSV file.

---

## 🚀 Features

- ✅ User form submission (name input)
- ✅ Stores data with timestamp in SQLite (`submissions.db`)
- ✅ Displays all submissions on the homepage
- ✅ Download all data as a CSV file
- ✅ Neat admin UI built with HTML templates

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **SQLite3**
- **HTML (Jinja templates)**

---

## 📂 Project Structure

flask-hello/
├── templates/
│ ├── form.html
│ └── form1.html
├── app.py # Main Flask app
├── test_sqlite.py # SQLite testing script
├── submissions.db # SQLite DB storing submissions
├── submissions.csv # CSV file for download
├── submissions.txt # (Optional) legacy log file
├── venv/ # Python virtual environment
└── README.md # 📄 You're reading this
---

## 🧪 How to Run Locally

**Clone the repo:**
```bash
git clone https://github.com/Decadent-tech/flask-hello.git
cd flask-hello
(Optional but recommended)

Create a virtual environment:

bash
python -m venv venv
source venv/Scripts/activate   # On Windows

**Install dependencies:**
pip install flask

Run the app:
python app.py

Open in browser:
http://localhost:5000/
📤 **Export Data**
Visit http://localhost:5000/download to download all submissions as a CSV file.

##🔒 **Admin View**
All form submissions are visible on the homepage.

Designed to simulate an internal dashboard.

##🤝 **Contributions**
Pull requests welcome. For major changes, open an issue first to discuss what you'd like to change.

📃 **License**
This project is licensed under the 

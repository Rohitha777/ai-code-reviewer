# 🤖 AI Code Reviewer

[![Open in Streamlit]] --> ai-code-reviewer-dizdaunz5jlyevvmffljsv
AI Code Reviewer is a web-based tool that automatically analyzes Python code to assess quality, maintainability, and style using industry-standard tools: Flake8, Radon, and Black. It provides a code quality score, suggestions, and a downloadable or emailable report — perfect for developers, students, and teams.

---

## 📌 Features

✅ Upload Python files or paste code  
🎯 Style analysis via Flake8 (PEP8 violations)  
📦 Complexity metrics with Radon  
🧼 Auto-formatting preview using Black  
📊 Code quality score & summary  
📩 Send review report via email  
📥 Download full report as .txt  
📄 Professional project report included (PDF)

---


## 🛠️ Tech Stack

- Python 3.10+
- Streamlit
- Flake8
- Radon
- Black
- smtplib (for sending emails)

---

## 🗂️ Folder Structure

ai-code-reviewer/
├── app.py
├── requirements.txt
├── README.md
├── your_logo.jpg
├── AI_Code_Reviewer_Project_Report.pdf
└── utils/
├── analysis.py
├── report.py
└── send_email.py


## 🚀 Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Rohitha777/ai-code-reviewer.git
cd ai-code-reviewer
Set up virtual environment:

Windows:

python -m venv .venv
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py

📬 Email Configuration
To enable email functionality:

Use an App Password (recommended for Gmail):
Go to your Google Account → Security → App Passwords → Generate one.

Open utils/send_email.py and replace:
sender_email = "youremail@gmail.com"
sender_password = "yourapppassword"
You’re set! The report will be sent to the entered user’s email.

🌐 Deploy on Streamlit Cloud
Push your project to GitHub

Go to https://streamlit.io/cloud

Click "New app" and connect your repo

Set the main file to app.py

Click "Deploy"

Done!



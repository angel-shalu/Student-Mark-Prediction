# 🎓 Student Mark Prediction Web App

A machine learning–powered web application that predicts student marks based on study hours.
Built with Python, Scikit-Learn, and Flask, and successfully deployed on Render.

# 🔗 Live Demo:
👉 https://student-mark-prediction-2.onrender.com


# ✨ Key Highlights

🤖 Machine Learning–based prediction

📊 Linear Regression model

🌐 Flask web application

🎨 Clean HTML (Jinja2) interface

🚀 Production deployment using Gunicorn

☁️ Hosted on Render (Cloud)


# 🧠 How It Works

User enters daily study hours (1–24)

Input is sent to a trained ML model

Model predicts expected marks

Result is displayed instantly on the same page


# 🛠️ Tech Stack
Layer	Technology
Programming Language	Python
Web Framework	Flask
ML Algorithm	Linear Regression
ML Library	Scikit-Learn
Data Handling	NumPy, Pandas
Templating	Jinja2
Server	Gunicorn
Deployment	Render

# 📂 Project Structure
Student-Mark-Prediction/
│
├── app.py                         # Flask application

├── student_mark_predictor.pkl     # Trained ML model

├── requirements.txt               # Project dependencies

├── templates/
│   └── index.html                 # Frontend UI

└── README.md


# ▶️ Run Locally
1️⃣ Clone the repository
git clone https://github.com/angel-shalu/Student-Mark-Prediction.git
cd Student-Mark-Prediction

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
python app.py


# Open your browser and visit:
👉 http://127.0.0.1:5000


# ☁️ Deployment Details (Render)

Runtime: Python 3.13

Build Command

pip install -r requirements.txt


Start Command

gunicorn app:app


The application is live and production-ready.


# 🧪 Sample Prediction
Study Hours	Predicted Marks
4	~45%
7	~70%
10	~90%

(Values depend on trained dataset)


# 👩‍💻 Author
Shalini Kumari
📌 Data Science & Machine Learning Enthusiast
🔗 GitHub: https://github.com/angel-shalu


# 🚀 Future Improvements

📈 Prediction history using database

🔐 User authentication

⚡ FastAPI backend

📱 Streamlit UI for ML portfolio

🤖 GenAI integration

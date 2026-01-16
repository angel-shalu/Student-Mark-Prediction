import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import joblib
import os
     
app = Flask(__name__)
model = joblib.load(os.path.join(os.path.dirname(__file__), "student_mark_predictor.pkl"))
     
df = pd.DataFrame()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = float(request.form['study_hours'])

        if hours < 1 or hours > 24:
            return render_template(
                'index.html',
                prediction_text='Please enter study hours between 1 and 24'
            )

        prediction = model.predict([[hours]])[0]

        return render_template(
            'index.html',
            prediction_text=f'You will get {prediction:.2f}% marks if you study {hours} hours per day'
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f'Error occurred: {e}'
        )

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

from flask import Flask, request, render_template
from ml.predictor import predict_marks

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        hours = float(request.form["study_hours"])

        if hours < 1 or hours > 24:
            return render_template(
                "index.html",
                prediction_text="Please enter study hours between 1 and 24"
            )

        prediction = predict_marks(hours)

        return render_template(
            "index.html",
            prediction_text=f"You will get {prediction:.2f}% marks if you study {hours} hours per day"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {e}"
        )

if __name__ == "__main__":
    app.run()

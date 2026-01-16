from .model_loader import load_model

model = load_model()

def predict_marks(hours: float) -> float:
    prediction = model.predict([[hours]])[0][0]
    return float(prediction)

import os
import joblib

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),   # ml/
    "..",                        # project root
    "student_mark_predictor.pkl"
)

def load_model():
    return joblib.load(MODEL_PATH)

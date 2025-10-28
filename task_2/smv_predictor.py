import joblib
from ai_model import AIModel

model = AIModel()
joblib.dump(model, "smv_predictor.joblib")

print("Model trained and saved as smv_predictor.joblib")

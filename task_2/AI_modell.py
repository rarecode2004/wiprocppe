import numpy as np
from sklearn.linear_model import LinearRegression

class AIModel:
    def __init__(self):
        # Train a simple model (Y = 2X + 3)
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([5, 7, 9, 11, 13])
        self.model = LinearRegression().fit(X, y)

    def predict(self, value):
        # Predict based on trained model
        X_input = np.array([[value]])
        prediction = self.model.predict(X_input)[0]
        return float(prediction)

if __name__ == "__main__":
    ai = AIModel()
    print(ai.predict(10))  

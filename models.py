"""This module trains scikit-learn models for emotion recognition."""

import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


def train_models():
    """Train and save the models."""
    print("Loading features...")
    X = joblib.load("features/X.joblib")
    y = joblib.load("features/y.joblib")

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train LSTM-like model (using MLPClassifier)
    print("Training LSTM-like model...")
    lstm_model = MLPClassifier(
        hidden_layer_sizes=(64, 32),
        activation='relu',
        solver='adam',
        max_iter=300,
        random_state=42
    )
    lstm_model.fit(X_train, y_train)
    print(f"LSTM-like model accuracy: {lstm_model.score(X_test, y_test):.2f}")

    # Train CNN-like model (using RandomForestClassifier)
    print("Training CNN-like model...")
    cnn_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    cnn_model.fit(X_train, y_train)
    print(f"CNN-like model accuracy: {cnn_model.score(X_test, y_test):.2f}")

    # Save models
    print("Saving models...")
    if not os.path.exists("models"):
        os.makedirs("models")
    joblib.dump(lstm_model, "models/lstm_model.joblib")
    joblib.dump(cnn_model, "models/cnn_model.joblib")
    print("Models saved successfully!")


if __name__ == "__main__":
    train_models()

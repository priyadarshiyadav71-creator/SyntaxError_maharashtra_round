import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


# Load dataset
df = pd.read_csv("./data/misconceptions.csv")

# Combine question and student answer
df["text"] = (
    df["question"] +
    " Student answer: " +
    df["student_answer"]
)

X = df["text"]
y = df["misconception"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.5,
    random_state=42,
    stratify=y
)


# ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])


# Train
model.fit(X_train, y_train)


# Evaluate
predictions = model.predict(X_test)

print(classification_report(y_test, predictions))


# Save model
joblib.dump(model, "./models/misconception_model.pkl")

print("Model saved successfully!")
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


SERVICE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = SERVICE_DIR / "data" / "misconceptions.csv"
MODEL_PATH = SERVICE_DIR / "models" / "misconception_model.pkl"

df = pd.read_csv(DATA_PATH).fillna("")
required_columns = {"question", "student_answer", "correct_answer", "misconception"}
missing_columns = required_columns.difference(df.columns)
if missing_columns:
    raise ValueError(f"Training data is missing columns: {sorted(missing_columns)}")
if df.empty:
    raise ValueError("Training data must contain at least one example.")

df["text"] = (
    df["question"] +
    " Student answer: " +
    df["student_answer"]
)
X = df["text"]
y = df["misconception"]

# Report a holdout estimate, then fit the deployed model on every supplied example.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

def create_model():
    return Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])

evaluation_model = create_model()
evaluation_model.fit(X_train, y_train)
predictions = evaluation_model.predict(X_test)
print(classification_report(y_test, predictions, zero_division=0))

model = create_model()
model.fit(X, y)
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"Trained on {len(df)} examples across {y.nunique()} misconception categories.")
print(f"Model saved to {MODEL_PATH}")
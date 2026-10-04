from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from interventions import INTERVENTIONS

app = FastAPI()
MIN_DIAGNOSIS_CONFIDENCE = 0.3
MIN_QUESTION_SIMILARITY = 0.2
QUESTION_SIMILARITY_MARGIN = 0.05
SERVICE_DIR = Path(__file__).resolve().parent
model = joblib.load(SERVICE_DIR / "models" / "misconception_model.pkl")
training_data = pd.read_csv(SERVICE_DIR / "data" / "misconceptions.csv").fillna("")
question_vectorizer = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
question_vectors = question_vectorizer.fit_transform(training_data["question"].astype(str))
question_labels = training_data["misconception"].to_numpy()
known_examples = {
    question.strip().casefold(): {
        "correct_answer": answer,
        "misconception": misconception,
    }
    for question, answer, misconception in zip(
        training_data["question"],
        training_data["correct_answer"],
        training_data["misconception"],
    )
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentResponse(BaseModel):
    question: str
    answer: str


def normalize_answer(value: str) -> str:
    return "".join(value.casefold().split()).rstrip(".!?")


@app.get("/")
def home():
    return {
        "message": "Re:Learn ML API is running"
    }


@app.post("/diagnose")
def diagnose(data: StudentResponse):
    text = (
        data.question +
        " Student answer: " +
        data.answer
    )

    known_example = known_examples.get(data.question.strip().casefold())
    correct_answer = known_example["correct_answer"] if known_example else None
    if known_example and normalize_answer(data.answer) == normalize_answer(correct_answer):
        return {
            "misconception": None,
            "confidence": 1.0,
            "is_correct": True,
            "correct_answer": correct_answer,
            "intervention": None,
        }

    probabilities = model.predict_proba([text])[0]
    best_index = int(probabilities.argmax())
    best_prediction = model.classes_[best_index]
    best_confidence = float(probabilities[best_index])

    if known_example:
        prediction = known_example["misconception"]
        class_index = list(model.classes_).index(prediction) if prediction in model.classes_ else None
        confidence = float(probabilities[class_index]) if class_index is not None else 1.0
    else:
        if best_confidence < MIN_DIAGNOSIS_CONFIDENCE:
            return {
                "misconception": None,
                "confidence": round(best_confidence, 3),
                "is_correct": None,
                "correct_answer": None,
                "intervention": None,
                "message": (
                    "I couldn't confidently match this question and answer to a "
                    "known misconception. Try adding more detail or rephrasing it."
                ),
            }
        prediction = best_prediction
        confidence = best_confidence

        question_similarities = cosine_similarity(
            question_vectorizer.transform([data.question]),
            question_vectors,
        )[0]
        closest_question_similarity = float(question_similarities.max())
        matching_category_similarity = float(
            question_similarities[question_labels == prediction].max()
        )
        if (
            closest_question_similarity < MIN_QUESTION_SIMILARITY
            or matching_category_similarity
            < closest_question_similarity - QUESTION_SIMILARITY_MARGIN
        ):
            return {
                "misconception": None,
                "confidence": round(best_confidence, 3),
                "is_correct": None,
                "correct_answer": None,
                "intervention": None,
                "message": (
                    "The predicted misconception does not match the topic of "
                    "your question. Try rephrasing the question or adding more detail."
                ),
            }

    intervention = INTERVENTIONS.get(prediction)

    if intervention:
        follow_ups = intervention["follow_ups"]
        next_question = next(
            (
                item for item in follow_ups
                if item["question"].strip().casefold() != data.question.strip().casefold()
            ),
            follow_ups[0],
        )
        intervention_response = {
            "title": intervention["title"],
            "explanation": intervention["explanation"],
            "example": intervention["example"],
            **next_question,
        }
    else:
        intervention_response = None

    return {
        "misconception": prediction,
        "confidence": round(float(confidence), 3),
        "is_correct": False if correct_answer is not None else None,
        "correct_answer": correct_answer,
        "intervention": intervention_response,
    }

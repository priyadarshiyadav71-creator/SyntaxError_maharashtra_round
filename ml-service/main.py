from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from interventions import INTERVENTIONS

app = FastAPI()
SERVICE_DIR = Path(__file__).resolve().parent
model = joblib.load(SERVICE_DIR / "models" / "misconception_model.pkl")
training_data = pd.read_csv(SERVICE_DIR / "data" / "misconceptions.csv").fillna("")
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
    prediction = (
        known_example["misconception"]
        if known_example
        else model.predict([text])[0]
    )
    confidence = probabilities[list(model.classes_).index(prediction)]
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

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("models/misconception_model.pkl")


class StudentResponse(BaseModel):
    question: str
    answer: str


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

    prediction = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]

    confidence = max(probabilities)

    return {
        "misconception": prediction,
        "confidence": round(float(confidence), 3)
    }
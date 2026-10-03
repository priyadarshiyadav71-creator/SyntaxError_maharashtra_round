import { useState } from "react";
import axios from "axios"

function App() {

  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState(null);

  const question = "What does range(5) produce?";

  async function submitAnswer() {

    try {
      const response = await axios.post("http://localhost:8000/diagnose", {
        question: question,
        answer: answer,
      });

      setResult(response?.data);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <>
      <main className="min-h-screen p-10">

        <h1 className="text-4xl font-bold">
          Re:Learn
        </h1>

        <p className="mt-10 text-xl">
          {question}
        </p>

        <input
          className="mt-5 w-full max-w-xl rounded-lg border p-4"
          placeholder="Enter your answer..."
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
        />

        <button
          onClick={submitAnswer}
          className="mt-5 rounded-lg bg-black px-6 py-3 text-white"
        >
          Submit Answer
        </button>

        {result && (
          <div className="mt-10 rounded-xl border p-6">

            <h2 className="text-2xl font-bold">
              AI Diagnosis
            </h2>

            <p className="mt-4">
              Misconception: {result.misconception}
            </p>

            <p>
              Confidence: {result.confidence}
            </p>

          </div>
        )}

      </main>

    </>
  )
}

export default App

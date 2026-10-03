import { useState } from "react";
import axios from "axios";
import { styles } from "./utils/style.js";
import { Navbar } from "./Components/Navbar.jsx";
import { Hero } from "./Components/Hero.jsx";
import { Footer } from "./Components/Footer.jsx";

function normalizeAnswer(value) {
  return value
    .trim()
    .toLowerCase()
    .replace(/\s+/g, "")
    .replace(/[.!?]+$/g, "");
}

function formatConfidence(value) {
  if (typeof value === "number") {
    const pct = value <= 1 ? value * 100 : value;
    return { label: `${Math.round(pct)}%`, pct: Math.min(100, Math.max(0, pct)) };
  }
  return { label: String(value ?? "—"), pct: null };
}


function Step({ n, title, children, last }) {
  return (
    <li className="relative flex gap-5 pb-10 last:pb-0">
      {!last && (
        <span aria-hidden="true" className="absolute left-[19px] top-11 h-[calc(100%-2.5rem)] w-px" style={{ background: "var(--ink)", opacity: 0.25 }} />
      )}
      <span
        className="rl-display flex h-10 w-10 shrink-0 items-center justify-center rounded-full text-lg font-bold"
        style={{ background: "var(--marker)", border: "1.5px solid var(--ink)" }}
      >
        {n}
      </span>
      <div>
        <h3 className="rl-display text-xl font-bold">{title}</h3>
        <p className="mt-1 max-w-xl leading-relaxed" style={{ color: "var(--ink-soft)" }}>{children}</p>
      </div>
    </li>
  );
}


function App() {
  const [answer, setAnswer] = useState("");
  const [submittedAnswer, setSubmittedAnswer] = useState("");
  const [result, setResult] = useState(null);
  const [question, setQuestion] = useState("");
  const [expectedAnswer, setExpectedAnswer] = useState(null);
  const [feedback, setFeedback] = useState("");
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function submitAnswer() {
    if (!question.trim() || !answer.trim() || isSubmitting) return;
    const submitted = answer.trim();

    setIsSubmitting(true);
    setError("");
    setFeedback("");

    try {
      const response = await axios.post("http://localhost:8000/diagnose", {
        question: question.trim(),
        answer: submitted,
      });

      const data = response.data;

      setSubmittedAnswer(submitted);
      setAnswer("");

      const normalizedAnswer = normalizeAnswer(submitted);
      const normalizedExpected = expectedAnswer
        ? normalizeAnswer(expectedAnswer)
        : null;
      const isCorrect =
        data.is_correct === true ||
        data.correct === true ||
        (normalizedExpected && normalizedAnswer === normalizedExpected);

      if (isCorrect) {
        setResult(null);
        setFeedback("Your concepts are crystal clear!");
        return;
      }

      setResult(data);
      setFeedback("");

      if (data.intervention?.question) {
        setQuestion(data.intervention.question);
        setExpectedAnswer(data.intervention.expected_answer ?? null);
      }
    } catch (error) {
      setError(
        error.response?.data?.detail ??
        error.message ??
        "Unable to send your answer to the ML server."
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  const confidence = result ? formatConfidence(result.confidence) : null;

  return (
    <div className="rl-root min-h-screen">
      <style>{styles}</style>

      <Navbar />

      <main>
        <Hero />

        {/*  Question & response */}
        <section id="practice" className="mx-auto max-w-6xl px-6 pb-24">
          <h2 className="rl-display text-3xl font-extrabold md:text-4xl">Practice a concept</h2>
          <p className="mt-3 max-w-xl" style={{ color: "var(--ink-soft)" }}>
            Type a question, then your answer. After each diagnosis, the
            follow-up question loads here so you can keep going.
          </p>

          <div className="mt-10 grid items-start gap-8 lg:grid-cols-2">
            {/* input side */}
            <div className="rl-card p-6 md:p-8">
              <label htmlFor="question" className="block text-lg font-semibold">
                Your question
              </label>
              <textarea
                id="question"
                rows={3}
                className="rl-input mt-3 resize-y"
                placeholder="Type your question here..."
                value={question}
                onChange={(e) => {
                  setQuestion(e.target.value);
                  setExpectedAnswer(null);
                  setResult(null);
                  setFeedback("");
                  setError("");
                }}
              />

              <label htmlFor="answer" className="mt-6 block text-lg font-semibold">
                Your answer
              </label>
              <input
                id="answer"
                className="rl-input mt-3"
                placeholder="Enter your answer..."
                value={answer}
                onChange={(e) => {
                  setAnswer(e.target.value);
                  setError("");
                }}
                onKeyDown={(e) => {
                  if (e.key === "Enter") submitAnswer();
                }}
              />

              <button
                onClick={submitAnswer}
                disabled={isSubmitting || !question.trim() || !answer.trim()}
                className="rl-btn mt-7"
              >
                {isSubmitting ? "Sending..." : "Submit Answer"}
              </button>

              {feedback && (
                <p className="mt-6 text-lg font-semibold" style={{ color: "var(--good)" }} role="status">
                  {feedback}
                </p>
              )}

              {error && (
                <p
                  className="mt-6 rounded-lg border p-3 text-sm"
                  style={{ color: "var(--bad)", borderColor: "var(--bad)", background: "#fdf0f2" }}
                  role="alert"
                >
                  {error}
                </p>
              )}
            </div>

            {/* response  */}
            <div className="space-y-6" aria-live="polite">
              {!result && !feedback && (
                <div className="rl-card-flat p-8" style={{ borderStyle: "dashed" }}>
                  <h3 className="rl-display text-xl font-bold">Your diagnosis appears here</h3>
                  <p className="mt-2" style={{ color: "var(--ink-soft)" }}>
                    Submit an answer and you'll see the misconception, the
                    correct answer, and a short lesson.
                  </p>
                </div>
              )}

              {result && (
                <div className="rl-card p-6 md:p-8">
                  <h3 className="rl-display text-2xl font-bold">Response</h3>

                  <p className="mt-4 text-sm font-semibold" style={{ color: "var(--bad)" }}>
                    Misconception
                  </p>
                  <p className="mt-1">
                    <span className="rl-marker">{result.misconception}</span>
                  </p>

                  {submittedAnswer && (
                    <>
                      <p className="mt-4 text-sm font-semibold" style={{ color: "var(--ink-soft)" }}>
                        Your answer
                      </p>
                      <p className="mt-1">{submittedAnswer}</p>
                    </>
                  )}

                  {result.correct_answer && (
                    <>
                      <p className="mt-4 text-sm font-semibold" style={{ color: "var(--good)" }}>
                        Correct answer
                      </p>
                      <p className="mt-1">{result.correct_answer}</p>
                    </>
                  )}

                  <p className="mt-4 text-sm font-semibold" style={{ color: "var(--ink-soft)" }}>
                    Confidence
                  </p>
                  <div className="mt-1 flex items-center gap-3">
                    {confidence.pct !== null && (
                      <div
                        className="h-2 w-40 overflow-hidden rounded-full"
                        style={{ background: "var(--line)" }}
                        role="img"
                        aria-label={`Confidence ${confidence.label}`}
                      >
                        <div className="h-full" style={{ width: `${confidence.pct}%`, background: "var(--ink)" }} />
                      </div>
                    )}
                    <span className="font-semibold">{confidence.label}</span>
                  </div>
                </div>
              )}

              {result?.intervention && (
                <div className="rl-card-flat p-6 md:p-8">
                  <h3 className="rl-display text-2xl font-bold">
                    {result.intervention.title}
                  </h3>

                  <p className="mt-4 leading-relaxed">
                    {result.intervention.explanation}
                  </p>

                  <p
                    className="mt-4 rounded-lg p-4 leading-relaxed"
                    style={{ background: "#fff8d1" }}
                  >
                    💡 Example: {result.intervention.example}
                  </p>

                  <hr className="my-6" style={{ borderColor: "var(--line)" }} />

                  <h4 className="rl-display text-xl font-bold">Try this:</h4>
                  <p className="mt-2">{result.intervention.question}</p>
                  <p className="mt-2 text-sm" style={{ color: "var(--ink-soft)" }}>
                    This question is now loaded in the form. Type your answer to continue.
                  </p>
                </div>
              )}
            </div>
          </div>
        </section>

        {/* working */}
        <section
          id="how-it-works"
          className="border-y py-24"
          style={{ background: "#fff", borderColor: "var(--line)" }}
        >
          <div className="mx-auto grid max-w-6xl gap-14 px-6 lg:grid-cols-5">
            <div className="lg:col-span-2">
              <h2 className="rl-display text-3xl font-extrabold md:text-4xl">How the model works</h2>
              <p className="mt-4 leading-relaxed" style={{ color: "var(--ink-soft)" }}>
                Re:Learn doesn't only mark an answer right or wrong. A machine
                learning model reads your question and your answer together
                and looks for the specific idea you may have misunderstood.
              </p>
              <p className="mt-4 leading-relaxed" style={{ color: "var(--ink-soft)" }}>
                The confidence score shows how sure the model is about its
                diagnosis. A low score means the answer was unclear, so treat
                that diagnosis as a hint rather than a verdict.
              </p>
            </div>

            <ol className="lg:col-span-3">
              <Step n={1} title="You send a question and an answer">
                Your text goes to the Re:Learn server running the model. Nothing
                is graded by keyword matching alone.
              </Step>
              <Step n={2} title="The model reads them together">
                It checks what your answer assumes about the topic, not only
                whether the final result matches.
              </Step>
              <Step n={3} title="A misconception is identified">
                If the answer is wrong, the model names the likely
                misconception behind it and gives the correct answer and a
                confidence score.
              </Step>
              <Step n={4} title="You get a short lesson">
                A targeted explanation and a worked example address that one
                misconception instead of the whole topic.
              </Step>
              <Step n={5} title="A follow-up question checks the fix" last>
                The follow-up loads into the form. Answer it correctly and
                you'll see that your concepts are clear. If not, the cycle
                repeats with a new diagnosis.
              </Step>
            </ol>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}

export default App;
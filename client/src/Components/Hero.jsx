 export  function Hero() {
  return (
    <section id="top" className="mx-auto grid max-w-6xl items-center gap-12 px-6 pb-20 pt-16 md:grid-cols-2 md:pt-24">
      <div>
        <h1 className="rl-display text-5xl font-extrabold leading-[1.05] md:text-6xl">
          A wrong answer tells us what you actually think.
        </h1>
        <p className="mt-6 max-w-md text-lg leading-relaxed" style={{ color: "var(--ink-soft)" }}>
          Ask any question and give your best answer. Re:Learn finds the
          misconception behind a mistake, explains it with an example, and
          asks a follow-up until the idea clicks.
        </p>
        <div className="mt-8 flex flex-wrap items-center gap-4">
          <a href="#practice" className="rl-btn inline-block">Try a question</a>
          <a href="#how-it-works" className="rl-link font-semibold">See how it works</a>
        </div>
      </div>

      {/* sample diagnosis: shows the product's real output shape */}
      <div className="rl-card p-6" aria-label="Example diagnosis">
        <p className="text-sm font-semibold" style={{ color: "var(--ink-soft)" }}>
          Question: Which is heavier, 1 kg of iron or 1 kg of cotton?
        </p>
        <p className="mt-4 text-lg">
          Your answer: <span className="rl-marker">Iron, because it is denser.</span>
        </p>
        <div className="mt-5 border-t pt-4" style={{ borderColor: "var(--line)" }}>
          <p className="text-sm font-semibold" style={{ color: "var(--bad)" }}>Misconception found</p>
          <p className="mt-1">Confusing density with weight.</p>
          <p className="mt-4 text-sm font-semibold" style={{ color: "var(--good)" }}>Correct answer</p>
          <p className="mt-1">They weigh the same: 1 kg each.</p>
        </div>
      </div>
    </section>
  );
}
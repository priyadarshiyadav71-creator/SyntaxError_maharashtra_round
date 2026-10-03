 export  const styles = `
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&display=swap');

:root {
  --paper: #f4f6fb;
  --card: #ffffff;
  --ink: #17214d;
  --ink-soft: #4b5578;
  --line: #d9deee;
  --marker: #ffe45c;
  --good: #1f8a64;
  --bad: #c2384a;
}

html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }

.rl-root {
  font-family: 'Instrument Sans', system-ui, sans-serif;
  color: var(--ink);
  background-color:#e6f1fb;
 
}
.rl-display { font-family: 'Bricolage Grotesque', 'Instrument Sans', sans-serif; letter-spacing: -0.02em; }
.rl-marker {
  background: linear-gradient(transparent 55%, var(--marker) 55%, var(--marker) 92%, transparent 92%);
  padding: 0 .15em;
}
.rl-card { background: var(--card); border: 1.5px solid var(--ink); border-radius: 14px; box-shadow: 5px 5px 0 var(--ink); }
.rl-card-flat { background: var(--card); border: 1.5px solid var(--line); border-radius: 12px; }
.rl-btn {
  background: var(--ink); color: #fff; border-radius: 10px; font-weight: 600;
  padding: .8rem 1.4rem; transition: transform .12s ease, box-shadow .12s ease;
  box-shadow: 3px 3px 0 var(--marker);
}
.rl-btn:hover:not(:disabled) { transform: translate(-1px,-1px); box-shadow: 4px 4px 0 var(--marker); }
.rl-btn:active:not(:disabled) { transform: translate(2px,2px); box-shadow: 1px 1px 0 var(--marker); }
.rl-btn:disabled { opacity: .45; cursor: not-allowed; }
.rl-input {
  width: 100%; background: #fff; border: 1.5px solid var(--line); border-radius: 10px;
  padding: .9rem 1rem; color: var(--ink); transition: border-color .12s ease;
}
.rl-input::placeholder { color: #8d95b3; }
.rl-input:focus { outline: 3px solid rgba(255,228,92,.9); outline-offset: 1px; border-color: var(--ink); }
.rl-link:hover { text-decoration: underline; text-underline-offset: 4px; }
.rl-link:focus-visible, .rl-btn:focus-visible { outline: 3px solid var(--marker); outline-offset: 3px; }
section[id] { scroll-margin-top: 90px; }
`;
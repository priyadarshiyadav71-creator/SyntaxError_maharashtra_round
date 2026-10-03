export function Navbar() {
  return (
    <header className="sticky top-0 z-20 border-b" style={{ background: "rgba(244,246,251,.92)", borderColor: "var(--line)", backdropFilter: "blur(8px)" }}>
      <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4" aria-label="Main">
        <a href="#top" className="rl-display rl-link text-2xl font-extrabold">
          Re:Learn
        </a>
        <ul className="flex items-center gap-6 text-sm font-medium sm:gap-8">
          <li><a href="#practice" className="rl-link">Practice</a></li>
          <li><a href="#how-it-works" className="rl-link">How it works</a></li>
        </ul>
      </nav>
    </header>
  );
}
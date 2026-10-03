export function Footer() {
    return (
        <footer className="border-t" style={{ borderColor: "var(--ink)", background: "var(--ink)", color: "#e6e9f7" }}>
            <div className="mx-auto grid max-w-6xl gap-8 px-6 py-12 sm:grid-cols-3">
                <div>
                    <p className="rl-display text-2xl font-extrabold text-white">Re:Learn</p>
                    <p className="mt-3 max-w-xs text-sm leading-relaxed" style={{ color: "#aab2d6" }}>
                        Learn from your mistakes by finding the thinking behind them.
                    </p>
                </div>
                <div>
                    <p className="text-sm font-semibold text-white">Explore</p>
                    <ul className="mt-3 space-y-2 text-sm">
                        <li><a href="#top" className="rl-link">Home</a></li>
                        <li><a href="#practice" className="rl-link">Practice</a></li>
                        <li><a href="#how-it-works" className="rl-link">How it works</a></li>
                    </ul>
                </div>
                <div>
                    <p className="text-sm font-semibold text-white">Good to know</p>
                    <p className="mt-3 text-sm leading-relaxed" style={{ color: "#aab2d6" }}>
                        Diagnoses come from a machine learning model and can be wrong.
                        Check important facts against a trusted source.
                    </p>
                </div>
            </div>
            <div className="border-t px-6 py-5 text-center text-sm" style={{ borderColor: "rgba(255,255,255,.15)", color: "#aab2d6" }}>
                © {new Date().getFullYear()} Re:Learn. All rights reserved.
            </div>
        </footer>
    );
}

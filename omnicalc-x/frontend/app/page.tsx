"use client";

import { useState } from "react";

export default function Home() {
  const [problem, setProblem] = useState("");
  const [result, setResult] = useState<string | null>(null);

  async function handleSolve() {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/solve`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ problem_text: problem }),
    });
    const data = await res.json();
    setResult(data.result);
  }

  return (
    <main style={{ padding: 32, fontFamily: "system-ui" }}>
      <h1>OmniCalc-X</h1>
      <textarea
        value={problem}
        onChange={(e) => setProblem(e.target.value)}
        placeholder="Enter a problem, or wire up the canvas capture for handwriting..."
        rows={4}
        style={{ width: "100%", maxWidth: 480 }}
      />
      <div style={{ marginTop: 12 }}>
        <button onClick={handleSolve}>Solve</button>
      </div>
      {result && <pre style={{ marginTop: 16 }}>{result}</pre>}

      <footer style={{ marginTop: 48, fontSize: 13, color: "#666" }}>
        <p>Designed and developed by Nikhil Chary Sriramoju</p>
        <p>
          <a href="https://github.com/Nikhil-creat" target="_blank" rel="noreferrer">
            GitHub
          </a>{" "}
          ·{" "}
          <a
            href="https://in.linkedin.com/in/nikhil-chary-sriramoju-95041b38a"
            target="_blank"
            rel="noreferrer"
          >
            LinkedIn
          </a>{" "}
          ·{" "}
          <a href="mailto:nikhilsriramoju66@gmail.com">nikhilsriramoju66@gmail.com</a>
        </p>
      </footer>
    </main>
  );
}

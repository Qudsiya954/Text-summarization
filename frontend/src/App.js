import { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    if (!text.trim()) return alert("Please enter some text!");

    setLoading(true);
    setSummary("");

    try {
      const response = await fetch("https://text-summary-backend.icymeadow-66425bc4.eastus.azurecontainerapps.io/summarize", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
      });

      const data = await response.json();
      setSummary(data.summary);
    } catch (error) {
      alert("Error connecting to backend");
    }

    setLoading(false);
  };

  const wordCount = text.trim() ? text.trim().split(/\s+/).length : 0;
  const summaryCount = summary.trim() ? summary.trim().split(/\s+/).length : 0;
  const reduction =
    wordCount && summaryCount
      ? Math.round((1 - summaryCount / wordCount) * 100)
      : 0;

  return (
    <div className="app">
      <h1 className="title">🧠 AI Text Summarizer</h1>

      <div className="panels">
        
        {/* INPUT PANEL */}
        <div className="panel">
          <h3>INPUT TEXT</h3>

          <div className="inner-box">
            <textarea
              placeholder="Paste your article here..."
              value={text}
              onChange={(e) => setText(e.target.value)}
            />
          </div>

          <p className="count">{wordCount} words</p>

          <button onClick={handleSummarize}>
            {loading ? "Summarizing..." : "Summarize"}
          </button>
        </div>

        {/* OUTPUT PANEL */}
        <div className="panel">
          <h3>SUMMARY</h3>

          <div className="inner-box output">
            {loading ? <div className="loader"></div> : summary}
          </div>

          {summary && (
            <div className="stats">
              <span>Original: {wordCount} words</span>
              <span>Summary: {summaryCount} words</span>
              <span>Reduction: {reduction}%</span>
            </div>
          )}
        </div>

      </div>
    </div>
  );
}

export default App;
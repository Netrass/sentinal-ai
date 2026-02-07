# 🛡️ Sentinel-AI: Predictive Data Observability

**Sentinel-AI** is an agentic observability engine designed to bridge the gap between reactive error logging and proactive resolution. Built with the **PostHog stack** in mind, it uses LLMs to predict and fix pipeline failures before they impact downstream analytics.

---

## 🚀 The Core Mission
In high-scale environments (like PostHog’s ClickHouse/BigQuery pipelines), traditional monitoring tells you *when* a pipeline is dead. **Sentinel-AI** tells you *why* it's dying and provides a pragmatic fix based on historical memory.

### Key Value Props:
* **Contextual RCA:** Moves beyond simple regex patterns to understand the "reasoning" behind a failure.
* **Retrievable Memory:** Uses RAG to "remember" how previous outages were fixed.
* **Actionable Fixes:** Generates code snippets (SQL/Python) for immediate remediation.

---

## 🛠️ The "Cracked" Tech Stack
* **Intelligence:** `Gemini-1.5-Flash` via `langchain-google-genai`
* **Vector Memory:** `ChromaDB` for persistent incident embeddings
* **Framework:** `LangChain` (Runnables & Prompt Templates)
* **Interface:** `Streamlit` for a real-time developer dashboard



---

## 🏗️ Architecture & Logic
Sentinel-AI operates as a **RAG-based agent**:
1.  **Ingestion:** Polls incoming error logs (simulated via UI).
2.  **Embedding:** Errors are converted into vectors using `models/embedding-001`.
3.  **Retrieval:** The agent queries **ChromaDB** for similar historical "fingerprints."
4.  **Reasoning:** Gemini-1.5-Flash synthesizes the new error with retrieved context to output a Root Cause Analysis (RCA).

---

## ⚡ Setup & Installation

1. **Clone & Install:**
   ```bash
   git clone [https://github.com/Netrass/sentinal-ai.git](https://github.com/Netrass/sentinal-ai.git)
   cd sentinal-ai
   pip install -r requirements.txt

2. **Environment Variables:**
   Create a .env file and add your key:
   GOOGLE_API_KEY= 'your_key_here'

3. **Run the Dashboard:**
   python -m streamlit run app.py

4. **Roadmap**
   [ ] Integration with ClickHouse system logs.

   [ ] Slack/Discord alerting for autonomous fixes.

   [ ] Predictive "Disk Full" alerts based on ingestion velocity.

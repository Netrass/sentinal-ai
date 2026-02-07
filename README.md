🛡️ Sentinel-AI
Agentic Observability for High-Scale Data Pipelines
Sentinel-AI is a predictive data reliability engine built to handle the complexities of modern CDPs. Instead of just alerting when a pipeline breaks, Sentinel-AI uses RAG (Retrieval-Augmented Generation) to analyze historical failures and provide instant, actionable Root Cause Analysis (RCA).

🎯 The Mission
At a company like PostHog, data ingestion is the product. Every failed BigQuery job or ClickHouse exception translates to lost customer insights. Sentinel-AI bridges this gap by turning "silent failures" into "solved tickets."

✨ Key Features
Semantic RCA: Uses Gemini-1.5-Flash to reason over complex error logs.

Institutional Memory: Powered by ChromaDB, it remembers past incident resolutions so the team never solves the same bug twice.

Low-Latency Insight: Optimized for speed to match the "bias for action" required in high-growth environments.

Scalable Stack: Built with the latest LangChain v0.3 ecosystem.

🛠️ Technical Architecture
Sentinel-AI operates as a closed-loop system:

Ingest: Collects error logs from data warehouses (BigQuery/ClickHouse).

Embed: Converts logs into high-dimensional vectors using text-embedding-004.

Retrieve: Queries the vector store for similar historical patterns.

Resolve: An LLM agent synthesizes the current error and historical context into a fix.

🚀 Quick Start
1. Prerequisites
Python 3.10+

Google AI Studio API Key (Gemini)

2. Installation
Bash
git clone https://github.com/Netrass/sentinal-ai.git
cd sentinal-ai
pip install -r requirements.txt
3. Environment Setup
Create a .env file in the root directory:

Plaintext
GOOGLE_API_KEY=your_api_key_here
4. Run the Dashboard
Bash
python -m streamlit run app.py
👨‍💻 Built for PostHog
This project was built to demonstrate:

Product Thinking: Solving the "Mean Time to Recovery" (MTTR) problem.

Technical Speed: Moving from concept to functional MVP in hours.

Modern AI Stack: Practical application of Vector DBs and LLM orchestration.

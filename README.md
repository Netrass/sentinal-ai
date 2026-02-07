> Sentinel-AI: Predictive Observability for PostHog Pipelines
Sentinel-AI is a proof-of-concept agentic observability engine designed to turn reactive error logs into proactive resolutions. It uses Gemini-1.5-Flash and ChromaDB to provide context-aware Root Cause Analysis (RCA) for high-scale data warehouses like ClickHouse and BigQuery.

> Why this exists
In a product-led company like PostHog, data ingestion is the lifeblood. When a pipeline fails, every minute of downtime is a gap in customer analytics. Sentinel-AI bridges the gap between a "403 Forbidden" error and a fix by:

Retrieving historical incident data via Vector Search.

Reasoning over the specific error context using LLMs.

Recommending pragmatic, code-ready fixes for engineers.

> The "Cracked" Stack
LLM: Gemini-1.5-Flash (via langchain-google-genai).

Vector Database: ChromaDB for persistent RAG memory.

Backend: Python 3.13 + langchain.

Frontend: Streamlit for an autonomous developer dashboard.

> Key Features
Agentic RCA: Moves beyond pattern matching to semantic understanding of error logs.

Persistent Learning: An "Inject Memory" feature that allows teams to train the agent on their specific infra quirks (e.g., ClickHouse disk pressure or BigQuery schema drift).

Async-First: Designed to fit into PostHog's "Small Team" workflow—automating the repetitive parts of the Support Hero role.

> Quick Start
Clone the repo: git clone https://github.com/YOUR_USERNAME/sentinel-ai.git

Install deps: pip install -r requirements.txt

Run it: python -m streamlit run app.py
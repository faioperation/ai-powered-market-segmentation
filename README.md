# Bahrain Statistical AI Agent — Enterprise Dashboard

The **Bahrain Statistical AI Agent** is a production-ready, modular, and containerized system designed for ingesting national statistical datasets (CSV/Parquet format), cleaning and integrating them into unified master data structures, and answering statistical queries using a hybrid of regex intent classification, data repository lookups, and OpenAI LLM fallbacks.

---

## 🚀 Key Features
- **Hybrid Intent Routing**: Low-latency pattern matching with LLM fallbacks on unstructured or complex queries.
- **Dynamic Data Ingestion**: Webhook endpoints that accept file uploads, remote URLs, or base64 files.
- **Plotly Data Visualizations**: A graphical interface rendering interactive charts directly from structured parquet query layers.
- **Automated Directory Watcher**: Detects new raw uploads, applies column hints, maps synonyms, and merges into master files securely.

---

## 🛠️ Technology Stack
- **Backend Language**: Python 3.11
- **User Interface**: Gradio 6.0.0
- **Ingestion API Service**: Flask 3.1.2
- **Data Engineering**: Pandas, PyArrow (Parquet)
- **Containerization**: Docker (multi-stage) & Docker Compose
- **AI Integrations**: OpenAI client library (GPT-4o-mini / GPT-4 models)
- **External Snippet Fetching**: SerpAPI, Microsoft Bing Search API

---

## 📁 Repository Structure
```
├── config/
│   ├── endpoints.json          # Target URLs for schedule-based external fetches
│   └── schemas.json            # Dynamic Column hints and regular expression mapping schema
├── bahrain_agent/
│   ├── agent.py                # Main public reasoning engine
│   ├── data_layer.py           # Loads CSV/Parquet files into in-memory DataRepository
│   ├── describe_layer.py       # Domain logic that translates queries into summaries
│   ├── nlu_router.py           # Classifies search intent and manages OpenAI fallbacks
│   └── query_layer.py          # Executes aggregations and filters over dataframes
├── data/
│   ├── incoming/               # Raw CSV landing directory
│   ├── bahrain_master/         # Unified, cleaned master files (Parquet & CSV format)
│   └── bahrain_master_backups/ # Automatically generated backups during replacing ingestion
├── scripts/
│   ├── auto_ingest_watcher.py  # Watchdog daemon script to watch incoming folder
│   ├── check_masters.py        # Inspects files in bahrain_master for sanity checks
│   ├── fetch_and_ingest_replace.py  # Endpoint scraper that downloads files from config
│   ├── ingest_and_prepare.py   # Primary ingestion logic mapping headers to schemas
│   └── webhook_receiver.py     # HTTP Endpoint for CSV ingestion
├── Dockerfile                  # Production multi-stage Docker build
├── docker-compose.yml          # Container configuration orchestrator
└── app.py                      # Main entrypoint UI application script
```

---

## ⚙️ Quick Start

### 1. Configure the Environment
Copy the example environment configuration:
```bash
cp ai-part/.env.example ai-part/.env
```
Populate the missing environment credentials such as `OPENAI_API_KEY` and `WEBHOOK_SECRET` inside the `.env` file.

### 2. Launch with Docker Compose
Run the pre-configured container ecosystem using Docker Compose:
```bash
# Run in production mode
docker compose -f ai-part/docker-compose.yml -f ai-part/docker-compose.prod.yml up -d --build
```
This launches:
- **Gradio Dashboard**: `http://localhost:7860`
- **Ingestion webhook API**: `http://localhost:5000`

---

## 🔒 Security & Performance Policies
- **Non-Root User Execution**: Container processes run under a dedicated `appuser` (UID: 10000) instead of root.
- **Rate-Limiting & Validation**: Webhook uploads enforce content validation, MD5 deduplication checks, and file size limits (50 MB max).
- **Concurrency Locks**: Threading locks prevent parallel run races on the master file writing paths.

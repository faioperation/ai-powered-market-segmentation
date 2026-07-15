#!/bin/bash
# ==============================================================================
# Entrypoint Script for Docker Container Execution
# Launches the webhook receiver background process and the Gradio frontend.
# ==============================================================================
set -e

echo "[entrypoint] Starting webhook receiver background service on port 5000..."
python scripts/webhook_receiver.py &

echo "[entrypoint] Launching Gradio Web UI dashboard on port 7860..."
python app.py

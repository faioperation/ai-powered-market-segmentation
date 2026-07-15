#!/usr/bin/env python3
# ==============================================================================
# Healthcheck Script for Docker Container Verification
# Pings the locally-running Gradio application to ensure responsiveness.
# ==============================================================================
import sys
import urllib.request
import os

port = os.getenv("GRADIO_PORT", "7860")
url = f"http://127.0.0.1:{port}/"

try:
    urllib.request.urlopen(url, timeout=5)
    print("Healthcheck status: OK")
    sys.exit(0)
except Exception as e:
    print(f"Healthcheck status: FAILED ({e})")
    sys.exit(1)

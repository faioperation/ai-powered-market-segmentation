# ==============================================================================
# Multi-stage Production Dockerfile for Bahrain Statistical AI Agent
# ==============================================================================

# --- Build Stage ---
FROM python:3.11-slim AS builder

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN grep -v "audioop-lts" requirements.txt > requirements_filtered.txt && \
    pip install --no-cache-dir --user -r requirements_filtered.txt

# --- Run Stage ---
FROM python:3.11-slim AS runner

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy python dependencies from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Create non-root application user/group for security
RUN groupadd -g 10001 appgroup && \
    useradd -u 10000 -g appgroup -m -s /bin/bash appuser

# Copy source code with correct permissions
COPY --chown=appuser:appgroup . .

# Ensure standard directories exist and are owned by appuser
RUN mkdir -p data/incoming data/bahrain_master logs tmp && \
    chown -R appuser:appgroup data logs tmp

USER appuser

# Expose Gradio App port (7860) and Webhook Receiver port (5000)
EXPOSE 7860
EXPOSE 5000

ENV PYTHONUNBUFFERED=1
ENV GRADIO_SERVER_NAME="0.0.0.0"
ENV GRADIO_PORT=7860

ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]

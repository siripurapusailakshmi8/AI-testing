# Multi-stage build for Selenium test automation

# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    chromium-browser \
    chromium-driver \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    chromium-browser \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p logs screenshots reports

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV HEADLESS=true
ENV BROWSER=chrome

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Run tests
CMD ["pytest", "tests/", "-v", "--tb=short", "--html=reports/report.html"]

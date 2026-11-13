# Vortex Telegram Bot — container image.
# Build:  docker build -t vortex-bot .
# Run:    docker compose up -d   (see docker-compose.yml)

FROM python:3.11-slim

# Keep Python output unbuffered and avoid writing .pyc files.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install runtime dependencies first (cached layer).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code and the prompt files.
COPY bot/ ./bot/
COPY prompts/ ./prompts/

# Writable data directory for the SQLite database and token state.
# (Overridden by the ./data:/app/data volume in docker-compose.yml.)
RUN mkdir -p /app/data

# Run as a non-root user; the data volume must be writable by uid 10001.
RUN useradd --uid 10001 --create-home vortex \
    && chown -R vortex:vortex /app
USER vortex

# The bot reads its config from .env (mounted via env_file in compose)
# and stores state in /app/data (DATABASE_PATH=data/moz_bot.db).
VOLUME ["/app/data"]

CMD ["python", "-m", "bot.main"]

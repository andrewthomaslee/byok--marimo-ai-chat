# --- Builder Stage ---
# Use the Python image to build our assets and dependencies
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

WORKDIR /app

# Install system dependencies needed for building
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && rm -rf /var/lib/apt/lists/*

# Install TailwindCSS
RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 && \
    chmod +x tailwindcss-linux-x64 && \
    mv tailwindcss-linux-x64 /usr/local/bin/tailwindcss

# Install Python dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-cache

# Copy the rest of the app source
COPY . .

# Compile CSS
RUN tailwindcss -i ./static/input.css -o ./static/output.css --minify

# --- Final Stage ---
# Start from a clean, small base image
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv ./.venv

# Copy the compiled CSS from the builder stage
COPY --from=builder /app/static/output.css ./static/output.css

# Copy the application code required for runtime
COPY main.py elms.py funcs.py models.py OpenRouter.py ./

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Run the app
EXPOSE 8000
CMD ["marimo","run","--host","0.0.0.0","--port","8000","main.py"]
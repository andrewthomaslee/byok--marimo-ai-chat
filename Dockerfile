# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Install the project into `/app`
WORKDIR /app

# Update system
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

#Install TailwindCSS
RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 && \
    chmod +x tailwindcss-linux-x64 && \
    mv tailwindcss-linux-x64 tailwindcss

COPY . /app
RUN uv sync --locked --no-dev --no-cache

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

RUN ./tailwindcss -i ./static/input.css -o ./static/output.css --minify

EXPOSE 8000
CMD ["marimo","run","--host","0.0.0.0","--port","8000","main.py"]
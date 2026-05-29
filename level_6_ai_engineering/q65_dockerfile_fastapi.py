# Q65 — Production: Dockerise a FastAPI App
# Every production AI service runs in a container. Know this cold.
#
# Task 1 — Write a Dockerfile for a FastAPI app:
#   - Base image: python:3.11-slim
#   - Working directory: /app
#   - Copy requirements.txt first (layer caching trick)
#   - Install dependencies
#   - Copy the rest of the app
#   - Expose port 8000
#   - CMD to run uvicorn
#
# Task 2 — Write a docker-compose.yml that runs:
#   - The FastAPI app (port 8000)
#   - A Redis container (port 6379)
#   - A Qdrant container (port 6333)
#   All on the same network so they can talk to each other.
#
# Task 3 — Write a .dockerignore file
#   List what should NOT be copied into the container.
#
# Create: Dockerfile, docker-compose.yml, .dockerignore
# Build: docker build -t my-ai-app .
# Run:   docker-compose up

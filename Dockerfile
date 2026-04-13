FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

COPY mcp_server.py /app/mcp_server.py
COPY skill.json /app/skill.json
COPY SKILL.md /app/SKILL.md
COPY README.md /app/README.md
COPY tests /app/tests

EXPOSE 8080

CMD ["python", "mcp_server.py"]

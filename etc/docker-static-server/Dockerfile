FROM python:3.7-slim

WORKDIR /app/
COPY static/ static/

ENTRYPOINT ["python3.7", "-m", "http.server"]
CMD ["--directory", "static/", "80"]
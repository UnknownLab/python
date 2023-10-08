FROM python:3.8.3-alpine

WORKDIR /app/
COPY static/ static/

ENTRYPOINT ["python", "-m", "http.server"]
CMD ["--directory", "static/", "80"]
FROM python:3.12-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ARG APP_VERSION=unknown
ENV APP_VERSION=${APP_VERSION}

EXPOSE 8080

CMD ["python", "main.py"]

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV API_KEY=api_key
ENV CAL_ID=cal_id
ENV GOOGLE_CREDENTIALS_JSON=path/to/file
ENV GOOGLE_CREDENTIALS_PICKLE=path/to/file

CMD ["python", "main.py"]
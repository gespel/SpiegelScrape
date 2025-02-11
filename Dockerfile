FROM python:3
LABEL authors="Sten Heimbrodt"

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
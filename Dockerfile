FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py

CMD [ "uvicorn", "main:app" , "--reload", "--host=0.0.0.0"]
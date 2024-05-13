FROM python:3.10-bullseye

WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install gunicorn3 -y

COPY confs/dependencies/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:main"]
# CMD ["python","main.py"]
FROM python:3.11.0

ADD main.py .

RUN pip install flask psutil

CMD ["python", "./main.py"]

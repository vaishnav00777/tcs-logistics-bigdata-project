FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install pandas flask matplotlib kafka-python pyspark
CMD ["python","api/app.py"]

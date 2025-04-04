FROM bitnami/spark:3.5.4

WORKDIR /app
COPY consumer.py .

CMD ["spark-submit","--master", "spark://spark-master:7077","--packages", "org.apache.spark:spark-streaming_2.12:3.5.4","consumer.py"]
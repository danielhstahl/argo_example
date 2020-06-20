FROM python:alpine3.6
ADD livytest.py livytest.py
ADD spark_test.scala spark_test.scala
RUN pip install requests
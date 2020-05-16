FROM python:3.7-alpine
ARG VERSION="0.1"

ADD requeriments.txt /tmp/
RUN pip install -r /tmp/requeriments.txt

COPY app.py /app.py

ENV MY_KEY="Hello from Dockerfile"
ENV foo="DevOps Peru"

RUN echo ${VERSION} > /etc/app_version

CMD /app.py

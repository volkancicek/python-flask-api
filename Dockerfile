FROM ubuntu:latest
MAINTAINER Volkan Cicek "volkancicek@outlook.com"
ENV host_ip=0.0.0.0
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get clean all
COPY . /app
WORKDIR /app
RUN pip install flask
RUN pip install flasgger
RUN pip install flask_api
ENTRYPOINT ["python"]
CMD ["app.py"]

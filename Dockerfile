FROM ubuntu:latest
MAINTAINER Michael Brooks "mickybroox@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
FROM ubuntu:latest
MAINTAINER Adonai Goncalves "agoncalves@inf.ufsm.br"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["qa/app.py"]
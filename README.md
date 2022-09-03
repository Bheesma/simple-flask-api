# Simple Flask API

Simple Flask based API for playing with Docker and Kubernetes.

## Run the app from local machine

* Execute the following commands:
```
cd src
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
flask run
```
* Browse http://localhost:5000

## Run the app from Docker container

* Build docker image and start the container
```
docker build -t flaskapi:1 .
docker run -p 8080:8080 -d flaskapi:1
```
* Browse http://localhost:8080


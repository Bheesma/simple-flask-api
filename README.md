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

## Run the app from Kubernetes (minikube)

* Run the following command to re-use the docker daemon from Minikube [Reference 1](https://minikube.sigs.k8s.io/docs/handbook/pushing/#1-pushing-directly-to-the-in-cluster-docker-daemon-docker-env) & [Reference 2](https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube)

```
eval $(minikube docker-env)
```

* Build the docker image

```
docker build -t flaskapi:1 .
```

* Create pod (Ref: [ImagePullPolicy](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy)). Image is already available locally so we set it to 'Never'
```
kubectl run apitest --image=flaskapi:1 --port=8080 --image-pull-policy=Never
```

* Port-Forward to allow browsing from localhost [Reference 1](https://stackoverflow.com/a/72452035)
```
kubectl port-forward pod/apitest 54080:8080
```

* Browse the following URLs: 
   * http://localhost:54080
   * http://localhost:54080/customer/2323
   

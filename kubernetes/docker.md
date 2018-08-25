# Useful commands

## generate image

```bash
docker build -t [imagename] ./folder/with/Dockerfile
```

## remove image

```bash
docker rm [containerid]
docker rmi [imageid]
```

## list images

```bash
docker images
```

## run image

```bash
docker run -p 3000:3000 [imagename]
docker run -d --name mongodb mongo:3.5

docker run -p 3000:3000 --link mongodb:alias -e MONGO_URL=mongodb [imagename]
```

## logs image

```bash
docker logs -f [containerid]
```

## docker hub

```bash
docker login
docker build -t sharkguto:/[imagename]:v1 .

docker push sharkguto:/[imagename]:v1
```

## repositories

[https://hub.docker.com/](https://hub.docker.com/)

## docker register azure

```bash
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ xenial main" | \
    sudo tee /etc/apt/sources.list.d/azure-cli.list
sudo apt install azure-cli

az login
az account set --subscription [id from az login]
az group create --name k8s-curso --location eastus
az acr create --resource-group k8s-curso --name gmftechdock --sku Basic
az acr list --resource-group k8s-curso --output table
echo "gmftechdock.azurecr.io"
az acr login --name gmftechdock
# mapping local image to remote acr
docker tag [imagename]:v1 gmftechdock.azurecr.io/[imagename]:v1
# docker push to azure
docker push gmftechdock.azurecr.io/[imagename]:v1
```

## container instance services azure

```bash
# from dockerhub
az container create --resource-group k8s-curso \
   --name mongodb --image mongo:latest \
   --cpu 1 --memory 1 \
   --port 27017 \
   --ip-address public
az container logs --resource-group k8s-curso --name mongodb
az container show --resource-group k8s-curso --name mongodb --query ipAddress.ip

# from acr azure
export ACR_CREDENTIALS=$(az acr credential show -n gmftechdock --query passwords[0].value | sed -r 's/\"//g')

az container create --resource-group k8s-curso \
   --name api-heroes --image gmftechdock.azurecr.io/api-heroes:v1 \
   --cpu 1 --memory 1 \
   --port 5000 \
   --environment-variables MONGO_URL=137.135.127.88 \
   --registry-username gmftechdock \
   --registry-password $ACR_CREDENTIALS \
   --ip-address public

az container show --resource-group k8s-curso --name api-heroes --query ipAddress.ip
az container logs --resource-group k8s-curso --name api-heroes
```

## azure AKS

```bash
az aks create -g k8s-curso \
   --name k8s-cluster \
   --dns-name-prefix k8s-cluster \
   --generate-ssh-keys \
   --node-count 2\
   --node-vm-size Standard_A1_v2

# install kubectl
az aks install-cli
az aks get-credentials --resource-group k8s-curso --name k8s-cluster
kubectl get nodes

az aks browse --resource-group k8s-curso --name k8s-cluster

```

## K8s pods

```bash
#create
kubectl run mongodb --image mongo:3.5 --port 27017
kubectl get pods

#delete
kubectl delete pod $(kubectl get pods | grep -i mongodb | tail -1 | awk '{print $1}')
kubectl get pods

#describe
kubectl describe pods $(kubectl get pods | grep -i mongodb | tail -1 | awk '{print $1}')
kubectl top pod $(kubectl get pods | grep -i mongodb | tail -1 | awk '{print $1}')
kubectl get pods --output=wide


# it will work only in public repos on hub.docker
kubectl run api-heroes \
   --image erickwendel/api-heroes:v1 \
   --env "MONGO_URL=10.244.1.6" \
   --env "PORT=5000" \
   --replicas 2

kubectl logs $(kubectl get pods | grep -i api-heroes | tail -1 | awk '{print $1}')
kubectl expose pod $(kubectl get pods | grep -i api-heroes | tail -1 | awk '{print $1}') \
   --port 5000 \
   --type LoadBalancer
```

## K8s pods - with manifesto and acr credentials

```bash
# with aks and acr
kubectl create secret docker-registry regcred \
   --docker-server="gmftechdock.azurecr.io" \
   --docker-username=gmftechdock \
   --docker-password=$ACR_CREDENTIALS
#create pod following manifesto
kubectl create -f heroes-pod.json
kubectl expose pod api-heroes-pod \
   --port 5000 \
   --type LoadBalancer

#delete by pod name
kubectl delete pod api-heroes-pod
#delete by version
kubectl delete pod -l version=v1
#logs
kubectl logs api-heroes-pod
#access bash
kubectl exec -it api-heroes-pod -- /bin/bash
# explain pods
kubectl explain pods

#export pod configuration in yaml or json
kubectl get pod api-heroes-pod -o yaml
kubectl get pod api-heroes-pod -o json | grep podIP
```

## K8s replicasets - with manifesto and acr credentials

```bash
# if there is a pod api-heroes it will join to replicaset
kubectl apply -f heroes-pod.replicaset.json
# try to change "replicas": 3 and apply again
kubectl apply -f heroes-pod.replicaset.json
kubectl get pod -w
# delete all pods in a replicaset
kubectl delete -f heroes-pod.replicaset.json
```

## K8s services

```bash
#list svc
kubectl get svc

#delete svc
kubectl delete svc api-heroes-pod

# use type NodePort only to access internally
kubectl expose -f heroes-pod.replicaset.json \
   --port 5000 \
   --type LoadBalancer

# wait for external-ip
kubectl get svc

# mongo will expose only internally -- manually
kubectl expose pod $(kubectl get pods | grep -i mongodb | tail -1 | awk '{print $1}') \
   --port 27017 \
   --type NodePort \
   --name mongo-svc

# or using manifesto
kubectl create -f mongodb-pod.json
kubectl create -f mongodb.svc.json

kubectl apply -f heroes-pod.replicaset.usingsvcmongo.json

# now update our api to use service too by manifesto file
kubectl create -f heroes.svc.json

#list replicasets
kubectl get rs
```

## K8s rolling update

```bash
#save config to rollback --change heroes.svc.json image version to latest and rollback to v1
kubectl apply -f heroes.svc.json --record

#get revision id
kubectl rollout history deployment api-heroes-deployment
# check if something still running
kubectl rollout status deployment api-heroes-deployment

# from get revision id do rollback
kubectl rollout undo deployment api-heroes-deployment --to-revision 3

#change image realtime
kubectl set image deployment api-heroes-deployment \
   api-heroes=gmftechdock.azurecr.io/api-heroes:latest \
   --record
kubectl get pods -w
kubectl set image deployment api-heroes-deployment \
   api-heroes=gmftechdock.azurecr.io/api-heroes:v1 \
   --record

#change deployment file realtime on-the-fly
kubectl edit deployment api-heroes-deployment --record
```

## Ingress Controllers - like api gateway

```bash
#following order
kubectl create -f nginx-default-backend.yaml
kubectl create -f ingress-controller-nginx.yaml
kubectl create -f nginx.yaml
kubectl create -f ingress-heroes.yaml

# show ingress
kubectl get ingress
kubectl describe ingress ingress-heroes

#test
curl -H "Host:mysite.com" 40.76.74.181
curl -XGET http://40.76.74.181/
```

## StatefulSet - storage - save data

```bash
kubectl apply -f mongo-tst.json
kubectl get sts
kubectl describe sts mongodb
```

## persistent volume

```bash
# create persistent volume
kubectl apply -f persistent-volume.json
kubectl get pv

# create claim rule
kubectl apply -f persistent-volume-claim.json

#app example
kubectl apply -f persistent-app.json
kubectl expose -f persistent-app.json --type LoadBalancer --port 3000
```

## namespace

```bash

kubectl get namespaces
kubectl create namespace production
kubectl create namespace development

# run in another namespace
kubectl --namespace development run nginx --image nginx

# set a default namespace (change)
kubectl config set-context $(kubectl config current-context) \
   --namespace development
kubectl get pods
# rollback
kubectl config set-context $(kubectl config current-context) \
   --namespace default

# in metadata you can add namespace field to set it
```

## azure OMS - monitoring log tool

```bash
#search on resource group by log analitycs and install
```

## kubedash - open monitoring tool

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes-retired/kubedash/master/deploy/bundle.yaml
```

## autoscaling

https://github.com/kubernetes-incubator/metrics-server

```bash
#clone metrics and install
https://github.com/kubernetes-incubator/metrics-server.git
for i in $(ls autoscaling/metrics-server/deploy/1.8+/); do kubectl apply -f autoscaling/metrics-server/deploy/1.8+/$i ; done

kubectl apply -f kubectl apply -f autoscaling/api-heroes-hpa.json
# 10% defined on limit ahead, max 10 pods min 5 pods
kubectl autoscale deployment api-heroes --cpu-percent 10 --max 10 --min 5

#list hpa - horizontal pods autoscale
kubectl get hpa

# test
export HOST_TEST=$(kubectl get svc | grep -i api-heroes | awk '{print $4}')
wrk -c 200 -t 4 http://$HOST_TEST:4000/heroes
```
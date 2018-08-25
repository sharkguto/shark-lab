# Kubernetes & Docker

## Docker

* Unify environments production and development
* Clean environment, running only necessary services
* reuse of images and share resources
* Dockerfile to configure deployment process

## Kubernetes

* Control multiple containers in multiple regions
* Control and automatize deployment and update proccess
* Autoreplacement, autorestart, autoreplication and autoscaling
* Rolling updates and load balancers

## Cluster

master and node

- kubelet -> inform master report
- container runtime -> docker images
- network proxy -> kube-proxy

## Pod

group of n containers, network, ...

example:

1. pod api-payment
2. pod api-receving
3. mongodb

## ReplicaSet

group of n pods

## Deploy

group of n replica sets

1. multiple versions running
2. blue green tests
3. rollback versions
4. based on replicasets, add better model of update and simplify rollbacks

## Stateful Set

## Horizontal Auto Scaler

## Secret

## Service Account

## Chart

## Service

## Ingress

## Daemon Set

## Config Map

## Volume Claim
#!/bin/bash

read cluster

# create a cluster
kind create cluster --name ${cluster} --config cluster.yml

node_name=$(kubectl get nodes | awk '{print $1}' | grep 'worker$')

# label the node
kubectl label nodes ${node_name} node=python-app-node

# docker image creation
docker build -t python-app:1 .

# docker image load
kind load docker-image python-app:1 --name ${cluster}

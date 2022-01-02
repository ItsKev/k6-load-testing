#!/bin/bash

kind create cluster --config configs/kind-config.yaml

helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

linkerd install | kubectl apply -f -
linkerd viz install | kubectl apply -f -

helm install argo-cd argo/argo-cd --namespace argo-cd --create-namespace --values configs/argo-cd-values.yaml
# Instructions

https://argoproj.github.io/docs/argo/demo.html

# MicroK8s
* `sudo curl -sSL -o /usr/local/bin/argo https://github.com/argoproj/argo/releases/download/v2.2.1/argo-linux-amd64`
* `sudo chmod +x /usr/local/bin/argo`
* `sudo snap install microk8s --classic`
* `sudo microk8s.status --wait-ready`
* `sudo microk8s.enable dns dashboard registry`
* `sudo microk8s.kubectl create ns argo`
* `sudo microk8s.kubectl apply -n argo -f argo.yaml`
* `sudo microk8s.kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=default:default`
* `sudo microk8s.kubectl -n argo port-forward deployment/argo-ui 8001:8001`
* `sudo microk8s.kubectl config view --raw > $HOME/.kube/config`

In a new terminal

* `argo submit --watch ./basic_task.yaml`
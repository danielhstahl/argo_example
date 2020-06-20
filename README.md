# Instructions

https://argoproj.github.io/docs/argo/demo.html


# Minikube

Requires Minikube 1.10 or greater.

* `minikube start` 
* `kubectl create namespace argo`
* `sudo curl -sSL -o /usr/local/bin/argo https://github.com/argoproj/argo/releases/download/v2.2.1/argo-linux-amd64`
* `sudo chmod +x /usr/local/bin/argo`
* `kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/install.yaml`
* `kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=default:default`
* `kubectl -n argo port-forward deployment/argo-server 2746:2746`
* go to `http://127.0.0.1:2746/workflows`



# Livy

* `sudo su -c 'echo -e "$(cat /etc/resolv.conf | grep nameserver | cut -d\  -f2)\tminikube.host" >> /etc/hosts'`
* `docker run -p 8998:8998 -e SPARK_MASTER="local[*]" -e DEPLOY_MODE=client davlum/livy:0.7.0-spark2.4.4`

* `docker build . -t phillyfan1138/livysubmit:v3`
* `docker push phillyfan1138/livysubmit:v3`
* `docker run --network="host" -e LOCAL=true phillyfan1138/livysubmit:v3`

# Use livy in argo

* `argo submit --watch ./basic_task.yaml`
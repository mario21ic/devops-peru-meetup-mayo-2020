# devops-peru-meetup-mayo-2020

Este repositorio contiene demo de Helm presentada en el meetup de DevOps Peru mayo 2020
Video: https://www.youtube.com/watch?v=8oV3ad2mr4Y&t=118m
Slides: https://www.slideshare.net/mario21ic/manejo-de-packages-en-kubernetes-con-helm

## Requisitos:
- Minikube https://github.com/kubernetes/minikube/releases
- Kubectl https://github.com/kubernetes/kubectl/releases
- Helm https://github.com/helm/helm/releases

## Clonar repositorio
```
$ git clone https://github.com/mario21ic/devops-peru-meetup-mayo-2020
```

## Python Demo
```
cd python/
```

Generar release demo1 
```
helm install demo1 ./helm
```

Listar todos los releases
```
helm list
```

Revisar los recursos desplegados
```
kubectl get pods,deploy,configmap,service
```

Obtener el manifest del release demo1 
```
helm get manifest demo1
```

Abrir la app y testear dandole f5 varias veces para probar el contador:
```
minikube service demo1-mycounter-counter-svc
```

Revisar el contenido del Chart y valores
```
cat helm/Chart.yaml
cat helm/values.yaml
```

Revisar el contenido archivos encargados de: configmap, deployments y services
```
cat helm/templates/configmap.yaml
cat helm/templates/deployment.yaml
cat helm/templates/service.yaml
```


Generar release demo2 con service de tipo "Load Balancer" y con dos replicas
```
helm install demo2 --set service.type="LoadBalancer" --set replicaCount=2 ./helm
```

Abrir la app y revisar que tiene el contador en 1, ademas dar varias veces f5 para verificar que es otro contador:
```
minikube service demo1-mycounter-counter-svc
```

Revisar el status de los recursos
```
kubectl get pods,deploy,configmap,service
```

Actualizar el release demo2 con la nueva imagen mario21ic/devopsperu:1.2
```
nano helm/Chart.yaml # dejar la ultima linea appVersion: 1.2
helm upgrade demo2 ./helm/
```

Abrir la app para verificar que ahora imprime la version 1.2
```
minikube service demo1-mycounter-counter-svc
```

Rollback del release demo2 a una revision especifica
```
helm status demo2
helm rollback demo2 3
```

Desinstalar un release y ver estado de los recursos
```
helm uninstall demo1
```

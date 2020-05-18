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
minikube service demo2-mycounter-counter-svc
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
minikube service demo2-mycounter-counter-svc
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

## Monitoreo con Prometheus y Grafana
Agregar repo stable
```
helm repo add stable https://kubernetes-charts.storage.googleapis.com
```

Generar release mymonit de prometheus
```
helm install mymonit stable/prometheus
helm install mydash stable/grafana
```

Encontrar la URL de Prometheus
```
export POD_NAME=$(kubectl get pods --namespace default -l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")
kubectl --namespace default port-forward $POD_NAME 9090
```
Abrir en browser http://localhost:9090
Pueden poner container_cpu_load_average_10s en el dashboard para probar.

Obtener clave de Grafana
```
kubectl get secret --namespace default mydash-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

Acceder a Grafana
```
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=grafana" -o jsonpath="{.items[0].metadata.name}")
kubectl --namespace default port-forward $POD_NAME 3000
```
Abrir en browser http://localhost:3000

Agregar en datasource:
Ir a http://localhost:3000/datasources/new escoger Prometheus
Y en URL poner http://mymonit-prometheus-server luego clic en el boton Save & Test

Agregar un dashboard:
Ir a http://localhost:3000/dashboard/import y escribir 893 en el "Grafana.com Dashboard"
Luego en la seccion Prometheus seleccionar nuestro datasource "Prometheus", finalmente clic en Import

Nota: Documentacion de ese dashboard https://grafana.com/grafana/dashboards/893



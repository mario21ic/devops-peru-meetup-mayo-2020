Docker compose
docker-compose up
browser: localhost:8080

K8s:
kubectl apply -f k8s/*.yaml
kubectl get configmap
kubectl get deploy
kubectl get svc
minikube service counter-svc

kubectl scale deploy counter-app --replicas=3
kubectl get pods


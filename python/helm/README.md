# Instructions #

```
helm install bsql ./
helm test bsql
helm ls
kubectl get all

helm install bsql2 --set replicaCount=3 ./
helm unsintall bsql2
```

### Export template
```
helm template bsql1 --set replicaCount=2 ./
```

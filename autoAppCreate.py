argocd app create darkstar \
  --repo https://github.com/mongodb/mongodb-kubernetes-operator \
  --path charts/mongodb-operator \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default \
  --sync-policy automated

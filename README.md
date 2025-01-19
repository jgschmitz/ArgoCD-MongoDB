### ArgoCD and MongoDB Deployment in Kubernetes
![ArgoCD MongoDB Deployment](https://drive.google.com/uc?id=1kWfwyKPI2aw3JMXG0QlnQ1Ogl2mkxqV0)


#### Step 1: Install ArgoCD

Create the argo namespace:
```
kubectl create namespace argocd
```

### Install ArgoCD using the official manifest
```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Check the status of ArgoCD pods
```
kubectl get pods -n argocd
```

#### Step 2: Expose the ArgoCD Server
### Option A: Use port-forwarding for local access
```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```
### Option B: Change the service type to LoadBalancer for external access
```
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
```

### Verify the external IP (if LoadBalancer is used)
```
kubectl get svc -n argocd
```

#### Step 3: Retrieve ArgoCD Admin Password
### Retrieve the default admin password
```
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d
```

#### Step 4: Install the ArgoCD CLI (Optional but Recommended)
### MacOS (using Homebrew)
```
brew install argocd
```
### Linux
```
curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
chmod +x /usr/local/bin/argocd
```
### Login to ArgoCD
```
argocd login localhost:8080 --username admin --password <password>
```

### Step 5: Deploy MongoDB using ArgoCD

1. Create an ArgoCD Application YAML:
```
# Save this as darkstar-application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: darkstar
  namespace: argocd
spec:
  destination:
    namespace: default
    server: https://kubernetes.default.svc
  source:
    path: charts/mongodb-operator
    repoURL: https://github.com/mongodb/mongodb-kubernetes-operator
    targetRevision: HEAD
  project: default
  syncPolicy:
    syncOptions:
      - CreateNamespace=true
      - no-submodules=true
    automated:
      prune: true
      selfHeal: true
```

2. Apply the YAML:
```
kubectl apply -f darkstar-application.yaml -n argocd
```

3. Verify the Application in the ArgoCD UI:
   - Access the UI at `https://localhost:8080` (or the external IP if LoadBalancer is used).
   - Login with the username `admin` and the password retrieved earlier.
   - Verify that the `darkstar` application is synced and healthy.

### Step 6: Validate MongoDB Deployment
```bash
# Check the status of the MongoDB Kubernetes resources
kubectl get all -n default

# Ensure all pods are running and the deployment is successful
kubectl logs -l app=mongodb-kubernetes-operator -n default
```

### Final Step: Enjoy Your ArgoCD-Powered MongoDB Deployment
Your deployment is complete and should resemble the screenshot at the top! You can manage your MongoDB cluster using the ArgoCD UI and monitor its health and synchronization status.


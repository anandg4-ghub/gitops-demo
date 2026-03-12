# GitOps Demo

End-to-end GitOps pipeline: GitHub → GitHub Actions → Docker Hub → ArgoCD → Kubernetes

## Architecture

```
PR → GitHub Actions (build & test)
       ↓ (on merge to main)
     Docker Build → Push to Docker Hub
       ↓
     Update k8s/deployment.yaml with new tag
       ↓
     ArgoCD detects change → Syncs to K8s cluster
```

## Setup

### 1. Docker Hub Secrets
Add these to GitHub repo → Settings → Secrets → Actions:
- `DOCKERHUB_USERNAME` — your Docker Hub username
- `DOCKERHUB_TOKEN` — Docker Hub access token (not password)

### 2. ArgoCD
```bash
# Install ArgoCD in your cluster
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Apply the ArgoCD Application
kubectl apply -f k8s/argocd-app.yaml
```

### 3. Make a change and create a PR
```bash
git checkout -b feature/my-change
# edit app/main.py
git add . && git commit -m "feat: my change"
git push origin feature/my-change
# Create PR, approve, merge → pipeline runs automatically
```

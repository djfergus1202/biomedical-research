# 🚀 BioMed Suite - Kubernetes Deployment Guide

## Overview
This guide shows how to deploy the BioMed Research Suite using Docker and Kubernetes, similar to modern cloud-native applications.

---

## 🐳 Option 1: Local Docker Deployment

### Prerequisites
- Docker Desktop installed
- Docker Compose installed

### Quick Start
```bash
# 1. Build and run with Docker Compose
docker-compose up --build

# 2. Access the application
# Backend API: http://localhost:5000
# Frontend: http://localhost:8080
```

### Individual Docker Commands
```bash
# Build the image
docker build -t biomed-suite:latest .

# Run backend container
docker run -d -p 5000:5000 --name biomed-backend biomed-suite:latest

# Check health
curl http://localhost:5000/api/health
```

---

## ☸️ Option 2: Kubernetes Deployment

### Prerequisites
- Kubernetes cluster (minikube, kind, or cloud provider)
- kubectl installed
- Docker registry (DockerHub, GitHub Container Registry, etc.)

### Step 1: Build and Push Docker Image
```bash
# Build image
docker build -t yourusername/biomed-suite:latest .

# Push to registry (DockerHub example)
docker login
docker push yourusername/biomed-suite:latest

# Or use GitHub Container Registry
docker tag biomed-suite:latest ghcr.io/yourusername/biomed-suite:latest
docker push ghcr.io/yourusername/biomed-suite:latest
```

### Step 2: Update Kubernetes Deployment
Edit `kubernetes-deployment.yaml` and update the image:
```yaml
image: yourusername/biomed-suite:latest
```

### Step 3: Deploy to Kubernetes
```bash
# Create namespace
kubectl create namespace biomed-suite

# Deploy the application
kubectl apply -f kubernetes-deployment.yaml -n biomed-suite

# Check deployment status
kubectl get deployments -n biomed-suite
kubectl get pods -n biomed-suite
kubectl get services -n biomed-suite
```

### Step 4: Access the Application

#### Local Cluster (minikube/kind):
```bash
# Port forward to access locally
kubectl port-forward svc/biomed-suite-service 8080:80 -n biomed-suite

# Access at http://localhost:8080
```

#### Cloud Provider (GKE/EKS/AKS):
```bash
# Get external IP
kubectl get svc biomed-suite-service -n biomed-suite

# Access using the EXTERNAL-IP
```

---

## 🏃 Option 3: Quick Local Kubernetes (using kind)

```bash
# Install kind
brew install kind  # Mac
# or
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64  # Linux

# Create cluster
kind create cluster --name biomed

# Load image into kind
kind load docker-image biomed-suite:latest --name biomed

# Deploy
kubectl apply -f kubernetes-deployment.yaml

# Port forward
kubectl port-forward svc/biomed-suite-service 8080:80
```

---

## 🎯 Option 4: One-Click Cloud Deployments

### Google Cloud Run
```bash
# Build and deploy
gcloud run deploy biomed-suite \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Azure Container Instances
```bash
# Create container instance
az container create \
  --resource-group myResourceGroup \
  --name biomed-suite \
  --image yourusername/biomed-suite:latest \
  --dns-name-label biomed-suite \
  --ports 5000
```

### AWS ECS with Fargate
```bash
# Create task definition
aws ecs register-task-definition \
  --cli-input-json file://ecs-task.json

# Create service
aws ecs create-service \
  --cluster default \
  --service-name biomed-suite \
  --task-definition biomed-suite:1 \
  --desired-count 2 \
  --launch-type FARGATE
```

---

## 📊 Kubernetes Monitoring & Management

### Check Application Status
```bash
# View pods
kubectl get pods -n biomed-suite

# Check logs
kubectl logs -f deployment/biomed-suite-backend -n biomed-suite

# Describe deployment
kubectl describe deployment biomed-suite-backend -n biomed-suite

# Check service endpoints
kubectl get endpoints -n biomed-suite
```

### Scale Application
```bash
# Scale backend replicas
kubectl scale deployment biomed-suite-backend --replicas=3 -n biomed-suite

# Enable autoscaling
kubectl autoscale deployment biomed-suite-backend \
  --min=2 --max=10 --cpu-percent=70 -n biomed-suite
```

### Update Application
```bash
# Update image
kubectl set image deployment/biomed-suite-backend \
  backend=yourusername/biomed-suite:v2.0 -n biomed-suite

# Watch rollout
kubectl rollout status deployment/biomed-suite-backend -n biomed-suite

# Rollback if needed
kubectl rollout undo deployment/biomed-suite-backend -n biomed-suite
```

---

## 🔧 Helm Chart Deployment (Advanced)

### Create Helm Chart
```bash
# Create chart
helm create biomed-suite

# Install
helm install biomed-suite ./biomed-suite-chart \
  --namespace biomed-suite \
  --create-namespace
```

### values.yaml Example
```yaml
backend:
  image:
    repository: yourusername/biomed-suite
    tag: latest
  replicas: 2
  service:
    type: LoadBalancer
    port: 80
  resources:
    limits:
      memory: 512Mi
      cpu: 500m
    requests:
      memory: 256Mi
      cpu: 250m

frontend:
  enabled: true
  replicas: 1
  
ingress:
  enabled: true
  hostname: biomed.example.com
```

---

## 🌐 Production Configurations

### Add Persistent Storage
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: biomed-storage
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

### Add Secrets Management
```bash
# Create secret for sensitive data
kubectl create secret generic biomed-secrets \
  --from-literal=api-key=your-key \
  --from-literal=db-password=your-password \
  -n biomed-suite
```

### Add Network Policies
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: biomed-network-policy
spec:
  podSelector:
    matchLabels:
      app: biomed-suite
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: biomed-suite
    ports:
    - protocol: TCP
      port: 5000
```

---

## 🔍 Troubleshooting

### Pod not starting
```bash
# Check events
kubectl describe pod <pod-name> -n biomed-suite

# Check logs
kubectl logs <pod-name> -n biomed-suite --previous
```

### Can't access service
```bash
# Check service endpoints
kubectl get endpoints biomed-suite-service -n biomed-suite

# Test from inside cluster
kubectl run test --image=busybox -it --rm --restart=Never -- wget -O- http://biomed-suite-service/api/health
```

### Image pull errors
```bash
# Create image pull secret
kubectl create secret docker-registry regcred \
  --docker-server=docker.io \
  --docker-username=<username> \
  --docker-password=<password> \
  --docker-email=<email> \
  -n biomed-suite

# Add to deployment
imagePullSecrets:
- name: regcred
```

---

## ⚡ Quick Commands Reference

```bash
# Docker
docker-compose up -d              # Start all services
docker-compose logs -f backend    # View logs
docker-compose down               # Stop all services

# Kubernetes
kubectl apply -f kubernetes-deployment.yaml    # Deploy
kubectl delete -f kubernetes-deployment.yaml   # Remove
kubectl get all -n biomed-suite               # View everything
kubectl port-forward svc/biomed-suite-service 8080:80  # Local access

# Scaling
kubectl scale deployment biomed-suite-backend --replicas=5
kubectl autoscale deployment biomed-suite-backend --min=2 --max=10

# Updates
kubectl set image deployment/biomed-suite-backend backend=new-image:tag
kubectl rollout restart deployment/biomed-suite-backend
```

---

## 🎯 Architecture Overview

```
Internet
    │
    ▼
Ingress/LoadBalancer
    │
    ├──► Frontend Service (Nginx)
    │    └── HTML/CSS/JS Files
    │
    └──► Backend Service
         ├── Pod 1 (Flask/Gunicorn)
         ├── Pod 2 (Flask/Gunicorn)
         └── Pod N (Autoscaled)
```

---

## 📈 Next Steps

1. **Add CI/CD**: GitHub Actions to auto-build and deploy
2. **Add monitoring**: Prometheus + Grafana
3. **Add logging**: ELK stack or Fluentd
4. **Add service mesh**: Istio for advanced networking
5. **Add backup**: Velero for disaster recovery
6. **Add security**: OPA for policy enforcement

---

## 🚀 Ready to Deploy!

Choose your deployment method:
- **Local testing**: Use docker-compose
- **Production**: Use Kubernetes
- **Quick cloud**: Use Cloud Run/ECS/ACI

Your BioMed Research Suite is now cloud-native and ready to scale! 🎉

# LinkedIn Demo Video Plan

## Goal

Create a short, fast-paced project showcase that proves the project works instead of only talking about tools.

Target length: **60-90 seconds**

Record in 16:9 landscape at 1080p.

## Recommended sequence

### 0-5 sec — Hook

On-screen text:

```text
I built an end-to-end DevOps project on AWS 🚀
Flask → Docker → Jenkins → Kubernetes → EKS → Prometheus → Grafana
```

Show the CloudCart homepage immediately.

### 5-12 sec — Application

Show the CloudCart UI in the browser.

Quickly scroll through the page.

Overlay:

```text
Python Flask application
Containerized with Docker
```

### 12-20 sec — GitHub

Open the GitHub repository and quickly show:

- README architecture
- app.py
- Dockerfile
- Jenkinsfile
- k8s/
- tests/

Overlay:

```text
Everything documented and version controlled
```

### 20-28 sec — CI/CD

Show Jenkins pipeline stages.

Focus on the successful build.

Overlay:

```text
Jenkins
✓ Checkout
✓ Tests
✓ Docker Build
✓ Image Push
```

Do not show credentials or tokens.

### 28-38 sec — Kubernetes / EKS

Show terminal:

```bash
kubectl get nodes
kubectl get pods
kubectl get svc
```

Highlight:

- 2 EKS worker nodes
- 3 Flask Pods Running
- PostgreSQL Pod Running
- LoadBalancer Service

Overlay:

```text
Amazon EKS
3 application replicas
PostgreSQL StatefulSet
```

### 38-47 sec — Persistent storage

Show:

```bash
kubectl get pvc
kubectl get pv
```

Overlay:

```text
Persistent PostgreSQL storage
Amazon EBS gp3
```

### 47-57 sec — Prometheus

Open Prometheus Targets.

Show the CloudCart targets in green `UP`.

Overlay:

```text
Prometheus scraping every CloudCart Pod
```

### 57-70 sec — Grafana

Open your CloudCart dashboard.

Show:

- Total Requests
- Request Rate
- Traffic by Endpoint
- P95 Response Time

Overlay:

```text
Real-time observability with Grafana
```

### 70-80 sec — Architecture

Show the Mermaid architecture diagram from GitHub README.

Slow zoom/pan across:

```text
GitHub → Jenkins → Docker → ECR → EKS
                         ↓
                 PostgreSQL + EBS
                         ↓
                Prometheus → Grafana
```

### 80-90 sec — End card

On-screen text:

```text
Built and debugged end-to-end.

Python | Docker | Jenkins | AWS | EKS
Kubernetes | PostgreSQL | Prometheus | Grafana

github.com/iam-vinod7/flask-notes-devops
```

## Suggested narration

> I built CloudCart as an end-to-end DevOps learning project. The application is built with Flask, tested with pytest, containerized with Docker, and integrated with Jenkins CI. I deployed it to Amazon EKS using an ECR image, ran three application replicas, and used a PostgreSQL StatefulSet backed by EBS gp3 storage. I exposed the app through an AWS Load Balancer and added Prometheus metrics with Grafana dashboards for request traffic and P95 latency. Along the way I debugged real issues including Kubernetes pod capacity, EBS CSI configuration, PostgreSQL storage initialization, rollouts, and monitoring connectivity.

## Recording checklist

Before recording:

- CloudCart public page open
- GitHub repository open
- Jenkins successful build open
- Prometheus targets open
- Grafana dashboard open
- Terminal already authenticated to EKS
- increase terminal font size
- close personal tabs and notifications
- hide AWS account IDs where possible
- never display passwords, tokens, access keys, kubeconfig contents, or real Secrets

## Terminal commands to prepare

```bash
kubectl get nodes
kubectl get pods
kubectl get svc
kubectl get pvc
kubectl get pv
```

## Editing style

Use quick cuts rather than a long screen recording.

Recommended:

- 2-5 seconds per scene
- subtle zoom into the important part
- short text overlays
- no long terminal typing
- show successful output already on screen
- keep background music low if narration is used
- finish with GitHub link

The strongest proof in the video is not the tool logos. It is showing the live application, successful Jenkins pipeline, healthy EKS Pods, Prometheus targets, and the Grafana dashboard.

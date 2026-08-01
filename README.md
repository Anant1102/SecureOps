Overview:

Built an end-to-end DevSecOps platform using Flask, Docker, Kubernetes, Helm, and GitHub Actions.
Automated CI pipeline integrating SAST, dependency scanning, container scanning, and DAST.
Containerized and orchestrated applications using Docker Compose and Kubernetes.
Implemented secure configuration management with ConfigMaps and Secrets.
Integrated multiple security tools (Bandit, Gitleaks, pip-audit, Trivy, OWASP ZAP) into the CI workflow.



📖 Project Overview

SecureOps Enterprise DevSecOps Platform

🏗 Architecture Diagram
Developer
     │
     ▼
GitHub Repository
     │
GitHub Actions
     │
──────────────────────────────────────────────
│ Checkout Repository                        │
│ Install Dependencies                       │
│ Unit Tests                                 │
│ Bandit (SAST)                              │
│ pip-audit                                  │
│ Docker Build                               │
│ Docker Push                                │
│ Docker Compose Up                          │
│ Health Check                               │
│ OWASP ZAP                                  │
│ Trivy                                      │
│ Helm Lint                                  │
│ Helm Template                              │
│                                            │
──────────────────────────────────────────────
  
Docker Hub
🐳 Docker Architecture
               Docker Compose

        ┌─────────────────────────┐
        │     Flask Backend       │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │     PostgreSQL 16       │
        └─────────────────────────┘

        
☸ Kubernetes Architecture


                    Ingress
                       │
            ┌──────────┴──────────┐
            │                     │
            ▼                     ▼
 Backend Service           PostgreSQL Service
            │                     │
      Backend Pods          PostgreSQL Pod

      
🔐 Security Pipeline
Source Code

↓

Bandit

↓

pip-audit

↓

Gitleaks

↓

Docker Build

↓

Trivy

↓

OWASP ZAP

↓

Secure Image
Features
JWT Authentication
Flask REST API
PostgreSQL
Docker
Docker Compose
Kubernetes
Helm
GitHub Actions
Bandit
pip-audit
Trivy
OWASP ZAP
Health Checks
ConfigMaps
Secrets
Ingress
Rolling Updates


📂 Folder Structure

Complete project tree.

⚙ Installation

Backend

Docker

Docker Compose

Kubernetes

Helm

GitHub Actions




📊 CI/CD Pipeline

Step-by-step explanation of every GitHub Actions stage.

🛡 Security Reports

Bandit

Trivy

Gitleaks

OWASP ZAP

📸 Screenshots

GitHub Actions

Docker

Kubernetes

Helm

ZAP Report

Trivy Report


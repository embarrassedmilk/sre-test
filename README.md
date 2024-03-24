# Test assessment for SRE position

## Prerequisites
 - Docker
 - KinD
 - helm
 - kubectl
 - Python 3.x

## Contents
The result of this assessment contains an Ansible playbook, which will:
 - Create a local k8s cluster (using KinD)
 - Setup Ingress on the cluster (nginx)
 - Create 2 Docker images - one for the Backend service, another - for the Data API
 - Load them to the cluster
 - Install the Helm chart

Helm chart contains:
 - Service and Deployment for both Backend and Data APIs
 - Configmap which contains external integration URL
 - Secret which contains external integration key (for demo purposes only)
 - Ingress which allows us to access the APIs without forwarding the ports for every service

## How to deploy (locally)
 - Create a new virtual environment: `python3 -m venv .venv`
 - Activate it: `source .venv/bin/activate`
 - Install Ansible and Kubernetes Python package: `pip3 install ansible kubernetes`
 - Start Ansible playbook `ansible-playbook ./deploy-playbook.yaml`
 - After it's finished, go to `http://localhost/backend/download_external_logs`, you should see the external URL and the secret. Please note that this is for the demo purposes only and I'm aware that secrets shouldn't be put in a plain text in the output.

## How to destroy
 - Resources can be destroyed by using another playbook: `ansible-playbook ./destroy-playbook.yaml`

## Other notes
 - In production, secrets shouldn't be stored in base64 format, but be backed by an actual secrets manager (e.g. Hashicorp Vault if it's on-prem or corresponding secrets manager in the cloud provider).
 - To improve the security, we can use RBAC to make sure only authorised parties would have access to the secret.
 - Helm templates can be generalized by using library charts: https://helm.sh/docs/topics/library_charts/
 - Helm charts can be tested, here's a good example: https://medium.com/@zelldon91/advanced-test-practices-for-helm-charts-587caeeb4cb
# Why Containers in short?
Containers are a lightweight form of virtualization that package an application and its dependencies together. They provide consistency across different environments, making it easier to develop, test, and deploy applications.

# Why containers in the cloud?
1. Microservices Architecture
2. Continuous Integration / Continuous Deployment (CI/CD)
    * Containers ensure “build once, run anywhere.”
3. Application Modernization
    * Legacy applications are containerized to move them to the cloud.
4. Hybrid and Multi-Cloud Deployments
    * The same container image can run:
        1. On-premises
        2. In private cloud
        3. Across multiple public clouds

# How Container are Managed in the Cloud
1. Build the Container Image
2. Store the Container Image in a cloud Registry
3. Deploy Containers on Cloud Infrastructure

# Orchestration: Managing Containers at Scale
In real cloud environments, containers are rarely run individually. Instead, they are managed by container orchestration platforms, most commonly Kubernetes.
Kubernetes in the Cloud
Cloud providers offer managed Kubernetes:
* Amazon EKS
* Azure AKS
* Google GKE

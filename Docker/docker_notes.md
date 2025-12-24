# Docker: Complete Guide from Basics to Advanced

## 1. What is Docker?

Docker is a platform that packages applications and their dependencies into lightweight, portable containers. A container is an isolated process that runs your application with everything it needs, sharing the host's kernel but maintaining its own filesystem, process tree, and network stack.

**Key Benefits:**
- **Lightweight**: Containers share the host kernel, making them much smaller than virtual machines
- **Portable**: Build once, run anywhere consistently
- **Isolated**: Each container runs independently without interfering with others
- **Efficient**: Fast startup times and minimal resource overhead

## 2. How Docker Works Under the Hood

### Docker Architecture

Docker uses a **client-server architecture**:
- **Docker Client**: The CLI you interact with (`docker` command)
- **Docker Daemon (dockerd)**: The background service that does the actual work
  - Manages containers
  - Builds images
  - Handles networks and storage
  - Communicates with the Docker CLI

When you run `docker run hello-world`, here's what happens:
1. Docker client contacts the Docker daemon
2. Docker daemon pulls the image from Docker Hub (if not local)
3. Docker daemon creates a container from that image
4. Docker daemon executes the container and streams output to the client

### Linux Kernel Features

Docker leverages Linux kernel features for containerization:

**Namespaces** → Provide isolation for:
- **PID**: Process tree isolation (container sees only its processes)
- **NET**: Network stack isolation (own interfaces, routing, firewall)
- **MNT**: Filesystem isolation
- **IPC**: Inter-process communication isolation
- **UTS**: Hostname isolation
- **USER**: User/group ID isolation

**cgroups** → Limit and control resources:
- CPU usage
- Memory allocation
- Disk I/O
- Network bandwidth

**Union Filesystems (OverlayFS)** → Enable layered container images for efficiency

**Capabilities & seccomp** → Apply security constraints

### What's Shared vs Isolated?

**✔ Shared with Host:**
- Linux Kernel
- Kernel modules
- System call interface
- Device drivers

**✖ Isolated per Container:**
- Filesystem (each container has its own root filesystem)
- Process tree (PID namespace)
- Network stack (own interfaces, routing, firewall)
- IPC mechanisms
- Hostname
- User accounts

## 3. Core Concepts

### Docker Images

A **Docker image** is a read-only template containing:
- Application code
- Runtime environment
- Libraries and dependencies
- Environment variables
- Configuration files

**Key Characteristics:**
- **Layered structure**: Each instruction in a Dockerfile creates a new layer
- **Immutable**: Once built, images don't change (ensures consistency)
- **Portable**: Run the same image across different environments
- **Template for containers**: Images become running containers when executed
- **Stored in registries**: Shared via Docker Hub, GitHub Container Registry, GitLab, etc.

**Size Comparison:**
- Alpine container: ~5 MB (minimal BusyBox, musl libc, apk)
- Ubuntu container: ~70-90 MB (bash, core utilities, libraries)
- Full Ubuntu OS: ~3-5 GB (includes kernel, drivers, systemd, services)

### Docker Containers

A **Docker container** is a running instance of an image. It includes:
- Minimal userspace required for the application
- Application binaries and libraries
- Dependencies

**What containers do NOT include:**
- Kernel (uses host kernel)
- Hardware drivers
- System services (cron, systemd, udev) unless explicitly added
- Init system (usually)

**Container Filesystem:**
- Uses image layers (shared, read-only)
- Has its own writable layer for changes
- Extremely lightweight due to layer reuse

### Docker Registry

A **Docker registry** is a remote server that stores and distributes Docker images:
- **Docker Hub**: Official public registry
- **GitHub Container Registry**: GitHub's image hosting
- **GitLab Container Registry**: GitLab's image hosting
- **Private registries**: Self-hosted or enterprise solutions

## 4. Getting Started

### Installation & Setup

```bash
# Check Docker version
sudo docker --version

# Check Docker daemon status
sudo systemctl status docker

# Start Docker daemon
sudo systemctl start docker

# Verify installation
sudo docker run hello-world
```

## 5. Dockerfile Instructions

A **Dockerfile** defines how to build a Docker image.

| Instruction | Example | Purpose |
|------------|---------|---------|
| `FROM` | `FROM node:20-alpine` | Specifies base image to build upon |
| `WORKDIR` | `WORKDIR /app` | Sets working directory inside container |
| `COPY` | `COPY . .` | Copies files from host to container |
| `RUN` | `RUN npm install` | Executes commands during image build |
| `ENV` | `ENV PORT=8080` | Sets environment variables |
| `EXPOSE` | `EXPOSE 8080` | Documents which ports container listens on |
| `USER` | `USER node` | Sets user for subsequent commands |
| `CMD` | `CMD ["node", "server.js"]` | Default command when container starts |
| `ENTRYPOINT` | `ENTRYPOINT ["/bin/bash"]` | Primary command (CMD becomes arguments) |
| `LABEL` | `LABEL maintainer="dev@example.com"` | Adds metadata to image |
| `VOLUME` | `VOLUME /data` | Creates mount point for external volumes |
| `HEALTHCHECK` | `HEALTHCHECK CMD curl -f http://localhost/` | Defines container health check |

### Example Dockerfile

```dockerfile
FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
```

## 6. Essential Docker Commands

### Image Management

```bash
# Build an image from Dockerfile
sudo docker build -t my_app .

# List all images
sudo docker images
# or
sudo docker image ls

# Remove an image
sudo docker rmi <image_name>

# Force remove an image
sudo docker rmi -f <image_name>

# Pull image from registry
docker pull <username>/my_app

# Tag an image
sudo docker tag my_app <username>/my_app

# Push image to registry
sudo docker push <username>/my_app

# Login to registry
sudo docker login
```

### Container Management

```bash
# Run a container from image
sudo docker run my_app

# Run container with port mapping
docker run -p 5000:5000 myserver

# Run container in detached mode with port mapping
docker run -d -p 8080:80 my-app:latest

# List running containers
sudo docker ps

# List all containers (including stopped)
sudo docker ps -a

# Stop a container (gracefully)
sudo docker stop <container_id>

# Kill a container (forcefully)
sudo docker kill <container_id>

# Remove a container
sudo docker rm <container_id>
```

### Getting Help

```bash
# Display general help
docker help

# Get help for specific command
docker <command> --help
```

## 7. Docker Compose

Docker Compose manages multi-container applications using a `docker-compose.yml` file.

```bash
# Build, create, and start services in detached mode
docker compose up -d

# Stop and remove containers, networks, and volumes
docker compose down
```

## 8. Network and Port Mapping

When running containers, you often need to expose ports:

```bash
# Map container port to host port
docker run -p <host_port>:<container_port> <image>

# Example: Map host port 5000 to container port 5000
docker run -p 5000:5000 myserver
```

The `-p` flag syntax: `-p HOST_PORT:CONTAINER_PORT`

## 9. Best Practices

1. **Use specific base image tags** (not `latest`) for reproducibility
2. **Minimize layers** by combining RUN commands
3. **Use .dockerignore** to exclude unnecessary files
4. **Run containers as non-root user** for security
5. **Keep images small** by using Alpine-based images
6. **One process per container** (follow microservices pattern)
7. **Use volumes** for persistent data
8. **Implement health checks** for production containers

## 10. Quick Reference

**Docker Workflow:**
1. Write Dockerfile
2. Build image: `docker build -t myapp .`
3. Run container: `docker run myapp`
4. Tag image: `docker tag myapp username/myapp`
5. Push to registry: `docker push username/myapp`
6. Pull and run anywhere: `docker pull username/myapp && docker run username/myapp`

**Remember:**
> A Docker container packages the minimal user space required to run an application, while sharing the host kernel. This makes containers lightweight, fast, and portable.
# Docker: Commands and Practical Guide

## 1. Installation and Setup

### Check Docker Installation
```bash
# Check Docker version
sudo docker --version
# or
docker -v

# Verify installation works
sudo docker run hello-world
```

### Manage Docker Daemon
```bash
# Check Docker daemon status
sudo systemctl status docker

# Start Docker daemon
sudo systemctl start docker

# Stop Docker daemon
sudo systemctl stop docker

# Restart Docker daemon
sudo systemctl restart docker

# Enable Docker to start on boot
sudo systemctl enable docker
```

## 2. Dockerfile Instructions

A Dockerfile defines how to build a Docker image. Here are the essential instructions:

### Basic Dockerfile Template

```dockerfile
# Specify base image
FROM python:3.11-alpine

# Set working directory inside container
WORKDIR /app

# Copy files from host to container
COPY . .

# Execute commands during image build
RUN pip install -r requirements.txt

# Set environment variables
ENV PORT=8080

# Document which ports container listens on
EXPOSE 8080

# Set user for subsequent commands (security)
USER appuser

# Default command when container starts
CMD ["python", "main.py"]
```

### Dockerfile Instructions Reference

| Instruction | Purpose | Example |
|------------|---------|---------|
| `FROM` | Specifies base image to build upon | `FROM node:20-alpine` |
| `WORKDIR` | Sets working directory inside container | `WORKDIR /app` |
| `COPY` | Copies files from host to container | `COPY . .` |
| `ADD` | Like COPY but can also extract tar files | `ADD archive.tar.gz /app/` |
| `RUN` | Executes commands during image build | `RUN npm install` |
| `ENV` | Sets environment variables | `ENV PORT=8080` |
| `EXPOSE` | Documents which ports container listens on | `EXPOSE 8080` |
| `USER` | Sets user for subsequent commands | `USER node` |
| `CMD` | Default command when container starts | `CMD ["node", "server.js"]` |
| `ENTRYPOINT` | Primary command (CMD becomes arguments) | `ENTRYPOINT ["/bin/bash"]` |
| `LABEL` | Adds metadata to image | `LABEL maintainer="dev@example.com"` |
| `VOLUME` | Creates mount point for external volumes | `VOLUME /data` |
| `HEALTHCHECK` | Defines container health check | `HEALTHCHECK CMD curl -f http://localhost/` |
| `ARG` | Defines build-time variables | `ARG VERSION=1.0` |

### Example Dockerfiles

**Python Application:**
```dockerfile
FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
```

**Python with Trixie Base:**
```dockerfile
FROM python:3.11.14-trixie
WORKDIR /app
COPY . .
EXPOSE 8080
CMD ["python", "main.py"]
```

**Simple Python Interactive:**
```dockerfile
FROM python:3.11.14-alpine3.23
CMD ["python3"]
```

## 3. Image Management Commands

### Building Images

```bash
# Build image from Dockerfile in current directory
sudo docker build -t <image_name> .

# Build with specific tag
sudo docker build -t <image_name>:<tag> .

# Build from specific Dockerfile path
sudo docker build -t my_app ./path/to/dockerfile

# Build with build arguments
sudo docker build --build-arg VERSION=1.0 -t my_app .

# Examples
sudo docker build -t my_app .
sudo docker build -t my-app ./main.py
docker build -t myapp:v1.0 .
```

**Note on `-t` flag:**
- `-t` assigns a human-readable name and optional version tag to the Docker image
- Syntax: `<image_name>:<tag>`
- If no tag is specified, Docker uses `latest` by default

**Note on Tags:**
- A tag is a version label attached to an image name
- It allows you to identify which exact variant of an image you want to use
- Examples: `myapp:v1.0`, `myapp:production`, `myapp:dev`

### Listing Images

```bash
# List all images
sudo docker images

# Alternative command
sudo docker image ls

# List images with specific filter
docker images <image_name>
```

### Removing Images

```bash
# Remove a single image
sudo docker rmi <image_name>

# Force remove image (even if containers exist)
sudo docker rmi -f <image_name>

# Remove multiple images
sudo docker rmi <image1> <image2> <image3>

# Remove all unused images
docker image prune

# Remove all images
docker image prune -a
```

### Tagging Images

```bash
# Rename/tag images in local registry
sudo docker tag <old_image_name> <new_image_name>:<tag>

# Tag for remote registry (Docker Hub)
sudo docker tag my_app myusername/my_app

# Tag with version
sudo docker tag my_app myusername/my_app:v1.0

# Tag for private registry
sudo docker tag my_app registry.company.com/my_app:latest
```

**Use Case for Tagging:**
- Useful when you want to push the image to a remote registry
- The new image name should include the registry URL or username as a prefix
- Example: `docker tag my_app myusername/my_app`

**Note on Redundancy:**
- No need to worry about redundancy in local registry
- Docker reuses image layers if they are already present
- Tagging doesn't duplicate data, just creates a new reference

## 4. Container Management Commands

### Running Containers

```bash
# Basic run
sudo docker run <image_name>

# Run with port mapping
sudo docker run -p <host_port>:<container_port> <image_name>

# Run in detached mode (background)
docker run -d <image_name>

# Run in detached mode with port mapping
docker run -d -p 8080:80 my-app:latest

# Run in interactive mode with terminal
sudo docker run -it <image_name>

# Run with custom name
docker run --name my_container <image_name>

# Run with environment variables
docker run -e PORT=8080 -e ENV=production <image_name>

# Run with volume mount
docker run -v /host/path:/container/path <image_name>

# Examples
sudo docker run my_python_app
sudo docker run -p 8080:8080 my-app
docker run -p 5000:5000 myserver
sudo docker run -it ubuntu bash
docker run <username>/my_python_app
```

**Port Mapping Explanation:**
- `-p` maps a port on the host to a port on the container
- Syntax: `-p <host_port>:<container_port>`
- Example: `docker run -p 8080:80 <image_name>` maps:
  - Port 8080 on the host → Port 80 on the container
- The container can access the outer world (including localhost) via the host machine
- The outer world cannot access the container unless ports are mapped using `-p` flag

**Interactive Mode Flags:**
- `-i` keeps STDIN open even if not attached
- `-t` allocates a pseudo-TTY (terminal)
- Together `-it` makes it possible to interact with the container via terminal
- Useful for running shells like bash or debugging

### Listing Containers

```bash
# List running containers
sudo docker ps

# List all containers (including stopped)
sudo docker ps -a

# List containers with specific format
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"
```

### Stopping Containers

```bash
# Stop a container gracefully (sends SIGTERM, then SIGKILL after timeout)
sudo docker stop <container_id>
sudo docker stop <container_name>

# Stop multiple containers
docker stop <container1> <container2>

# Stop all running containers
docker stop $(docker ps -q)

# Kill a container immediately (sends SIGKILL)
sudo docker kill <container_id>
```

### Removing Containers

```bash
# Remove a stopped container
sudo docker rm <container_id>
sudo docker rm <container_name>

# Force remove a running container
docker rm -f <container_id>

# Remove multiple containers
docker rm <container1> <container2>

# Remove all stopped containers
docker container prune

# Remove container automatically after it stops
docker run --rm <image_name>
```

### Container Logs and Inspection

```bash
# View container logs
docker logs <container_id>

# Follow logs in real-time
docker logs -f <container_id>

# View last N lines of logs
docker logs --tail 100 <container_id>

# Inspect container details
docker inspect <container_id>

# View container resource usage
docker stats <container_id>

# Execute command in running container
docker exec -it <container_id> bash
docker exec -it <container_id> sh
```

## 5. Registry Operations

### Docker Hub Operations

```bash
# Login to Docker Hub
sudo docker login
docker login

# Login with username
docker login -u <username>

# Pull image from Docker Hub
docker pull <username>/my_app
docker pull ubuntu:22.04

# Tag image for Docker Hub
sudo docker tag my_python_app <docker_username>/my_python_app

# Push image to Docker Hub
sudo docker push <docker_username>/my_python_app

# Logout from Docker Hub
docker logout
```

### Working with Remote Images

```bash
# Pull image from registry
docker pull <username>/my_python_app

# Run image from registry
docker run <username>/my_python_app

# Complete workflow example
docker pull myusername/my_app
docker run myusername/my_app
```

## 6. Docker Compose Commands

Docker Compose manages multi-container applications using a `docker-compose.yml` file.

```bash
# Build, create, and start services in detached mode
docker compose up -d

# Start services (without rebuilding)
docker compose up

# Stop and remove containers, networks, and volumes
docker compose down

# View running services
docker compose ps

# View service logs
docker compose logs

# Follow logs in real-time
docker compose logs -f

# Rebuild services
docker compose build

# Restart services
docker compose restart
```

## 7. Getting Help

```bash
# Display general Docker help
docker help

# Get help for specific command
docker <command> --help

# Examples
docker build --help
docker run --help
docker ps --help
```

## 8. Complete Workflow Examples

### Example 1: Simple Python App

```bash
# 1. Create Dockerfile
# (see Dockerfile Instructions section)

# 2. Build the image
sudo docker build -t my_app .

# 3. List images to verify
sudo docker image ls

# 4. Run the container
sudo docker run my_app

# 5. Check running containers
sudo docker ps

# 6. Stop the container
sudo docker stop <container_id>

# 7. Remove the container
sudo docker rm <container_id>
```

### Example 2: Web Application with Port Mapping

```bash
# 1. Build the image
sudo docker build -t my-app .

# 2. Run with port mapping
sudo docker run -p 8080:8080 my-app

# 3. Access application at http://localhost:8080
```

### Example 3: Push to Docker Hub

```bash
# 1. Build the image
sudo docker build -t my_python_app .

# 2. Login to Docker Hub
sudo docker login

# 3. Tag the image for Docker Hub
sudo docker tag my_python_app <docker_username>/my_python_app

# 4. Push to Docker Hub
sudo docker push <docker_username>/my_python_app

# 5. Pull and run from anywhere
docker pull <docker_username>/my_python_app
docker run <docker_username>/my_python_app
```

### Example 4: Interactive Container

```bash
# Run Ubuntu container with interactive bash shell
docker run -it ubuntu bash

# Run Alpine container with interactive shell
docker run -it alpine sh

# Run Python container interactively
docker run -it python:3.11-alpine python3
```

## 9. Quick Reference Card

### Essential Commands Cheat Sheet

```bash
# Installation & Setup
docker --version                          # Check version
systemctl status docker                   # Check daemon status
systemctl start docker                    # Start daemon

# Image Commands
docker build -t <name> .                  # Build image
docker images                             # List images
docker rmi <image>                        # Remove image
docker tag <old> <new>                    # Tag image
docker pull <image>                       # Pull from registry
docker push <image>                       # Push to registry

# Container Commands
docker run <image>                        # Run container
docker run -d -p 8080:80 <image>         # Run detached with ports
docker run -it <image> bash              # Run interactive
docker ps                                 # List running containers
docker ps -a                              # List all containers
docker stop <container>                   # Stop container
docker rm <container>                     # Remove container
docker logs <container>                   # View logs
docker exec -it <container> bash         # Access running container

# Registry Commands
docker login                              # Login to Docker Hub
docker pull <user>/<image>               # Pull image
docker push <user>/<image>               # Push image

# Compose Commands
docker compose up -d                      # Start services
docker compose down                       # Stop services
docker compose logs -f                    # Follow logs

# Cleanup Commands
docker image prune                        # Remove unused images
docker container prune                    # Remove stopped containers
docker system prune                       # Clean up everything
```

## 10. Common Flags Reference

| Flag | Description | Example |
|------|-------------|---------|
| `-t` | Tag/name for image | `docker build -t myapp .` |
| `-p` | Port mapping | `docker run -p 8080:80 myapp` |
| `-d` | Detached mode (background) | `docker run -d myapp` |
| `-it` | Interactive with terminal | `docker run -it ubuntu bash` |
| `-i` | Keep STDIN open | `docker run -i myapp` |
| `-e` | Environment variable | `docker run -e PORT=8080 myapp` |
| `-v` | Volume mount | `docker run -v /host:/container myapp` |
| `-f` | Force operation | `docker rm -f container_id` |
| `--name` | Container name | `docker run --name web myapp` |
| `--rm` | Remove container after stop | `docker run --rm myapp` |
| `-a` | Show all (including stopped) | `docker ps -a` |

## 11. Best Practices

**Building Images:**
- Always use specific tags, not `latest`
- Use `.dockerignore` to exclude unnecessary files
- Minimize number of layers by combining commands
- Use multi-stage builds for smaller images

**Running Containers:**
- Always use `-d` flag for production services
- Always map ports explicitly with `-p`
- Use `--name` to give containers meaningful names
- Use `--rm` for temporary containers
- Use volumes (`-v`) for persistent data

**Security:**
- Don't run containers as root
- Use official base images
- Keep images updated
- Scan images for vulnerabilities

**Operations:**
- Use Docker Compose for multi-container apps
- Implement health checks
- Monitor container logs regularly
- Clean up unused images and containers
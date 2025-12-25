* Dockerfile: is the blue print of image
* image is the actual storage or collection of files
* container is the running image
# Docker 
1. sudo docker --version
2. sudo systemctl status docker
3. sudo systemctl start docker
2. create a Dockerfile
    1. From {base image}
    2. WORKDIR /app
    3. COPY . .
    4. CMD ["main.py"]
3. sudo docker build -t my_app . {image building}
4. sudo docker image ls{or images}
5. sudo docker rmi <image name> or sudo docker rmi -f <image name>
6. sudo docker run my_python_app
7. sudo docker ps
8. sudo docker stop <container id {or name}>
9. sudo docker rm <container id>

10. sudo docker login
11. sudo docker tag my_python_app <docker Uname>/my_python_app
12. sudo docker push <docker Uname>/my_python_app
13. docker pull <Uname>/my_python_app
14. docker run <uUname>/my_python_app


The Docker daemon (also called dockerd) is the background service that makes Docker work. It’s the core engine that:

manages containers

builds images

handles networks

manages storage

communicates with the Docker CLI

In simple terms:

Docker daemon = the backend engine that actually runs containers.

sudo docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

A Docker image is a read-only template containing an application and all its dependencies, including the code, runtime, libraries, environment variables, and configurations. It acts as a blueprint for creating Docker containers.

Layered structure: Docker images are built in layers, where each layer represents a change or instruction in the image's creation process (often defined in a Dockerfile). This layering enables efficient storage and reuse.
Immutable: Once an image is built, it is immutable, meaning it cannot be changed. This ensures consistency and reproducibility.
Portable: Images are designed to be portable, allowing you to build an image once and run it consistently across different environments, including your local machine, cloud platforms, or other servers.
Template for containers: An image is the foundation from which Docker containers are launched. When you run an image, it becomes a running instance called a container.
Stored in registries: Docker images are typically stored in registries, such as Docker Hub, which serve as central repositories for sharing and distributing images.


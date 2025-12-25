* create a docker file using base image and the application code

* build image using: sudo docker build -t <image_name> .
    * -t assigns a human-readable name and optional version tag to the Docker image. eg: docker build -t <image_name>:<tag> .
    * In Docker, a tag is a version label attached to an image name. It allows you to identify which exact variant of an image you want to use.

* run the image(make it container) using: sudo docker run -p <host_port>:<container_port> <image_name>
    * -p maps a port on the host to a port on the container. eg: docker run -p 8080:80 <image_name> maps port 8080 on the host to port 80 on the container.
    * remember the container can access the outer world (including localhost) via the host machine but the outer world cannot access the container unless we map the ports using -p flag.

* rename images in local registry using: sudo docker tag <old_image_name> <new_image_name>:<tag>
    * this is useful when you want to push the image to a remote registry like Docker Hub or a private registry. The new image name should include the registry URL or username as a prefix. eg: docker tag my_app myusername/my_app


* remember there is no need to care about redundancy in local registry because it reuses image layers if they are already present.

* use it flag to work container in interactive mode: sudo docker run -it <image_name> 
    * -i keeps STDIN open even if not attached.
    * -t allocates a pseudo-TTY (terminal) which makes it possible to interact with the container via terminal.

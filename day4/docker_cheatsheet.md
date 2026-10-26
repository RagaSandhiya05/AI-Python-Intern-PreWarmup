# 🐳 Docker CLI Cheatsheet

A quick reference to essential Docker commands used to manage images, containers, and application environments.

## 1. Check Docker Installation

| Command | Description |
|---|---|
| `docker --version` | Displays the installed Docker version. |
| `docker info` | Displays Docker engine information. |
| `docker compose version` | Displays the Docker Compose version. |

## 2. Docker Image Commands

| Command | Description |
|---|---|
| `docker images` | Lists locally available images. |
| `docker pull nginx` | Downloads the Nginx image from Docker Hub. |
| `docker rmi IMAGE_NAME` | Removes a local image, if unused. |

## 3. Docker Container Commands

| Command | Description |
|---|---|
| `docker run hello-world` | Runs a test container. |
| `docker ps` | Lists running containers. |
| `docker ps -a` | Lists all containers, including stopped ones. |
| `docker run -d --name my-nginx -p 8080:80 nginx` | Starts Nginx in the background and maps port 8080 on the host to port 80 in the container. |
| `docker stop CONTAINER_NAME` | Stops a running container. |
| `docker start CONTAINER_NAME` | Starts a stopped container. |
| `docker restart CONTAINER_NAME` | Restarts a container. |
| `docker rm CONTAINER_NAME` | Removes a stopped container. |
| `docker logs CONTAINER_NAME` | Displays container logs. |
| `docker exec -it CONTAINER_NAME sh` | Opens a shell inside a running container, if available. |

## 4. Docker Cleanup Commands

| Command | Description |
|---|---|
| `docker container prune` | Removes stopped containers after confirmation. |
| `docker image prune` | Removes unused dangling images after confirmation. |
| `docker system df` | Shows Docker disk usage. |

## 5. Docker Compose Commands

| Command | Description |
|---|---|
| `docker compose up` | Creates and starts services defined in a Compose file. |
| `docker compose up -d` | Starts services in the background. |
| `docker compose ps` | Lists containers managed by Compose. |
| `docker compose logs` | Displays service logs. |
| `docker compose down` | Stops and removes Compose-managed containers and networks. |

## Key Takeaways

- **Image:** A template used to create containers.
- **Container:** An isolated environment in which an application runs.
- **Port mapping:** Connects a host port to a container port.
- **Docker Compose:** Manages applications containing multiple services.

*Note: Replace placeholders such as `CONTAINER_NAME` and `IMAGE_NAME` with the actual names or IDs. Cleanup commands can remove resources, so use them carefully.*
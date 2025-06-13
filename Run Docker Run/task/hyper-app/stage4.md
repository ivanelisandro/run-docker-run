# Stage 4:

In this stage we will run the container from the image we built in the previous stage.

Once running, the application should be available at:

- http://localhost:8000/

Useful links:

- https://docs.docker.com/engine/reference/run/
- https://docs.docker.com/engine/reference/run/#detached-vs-foreground
- https://docs.docker.com/engine/network/

## Objectives

- The image for the container should be `hyper-web-app`;
- Run the container in the `detach` mode;
- Map container port `8000` to the host port `8000`.

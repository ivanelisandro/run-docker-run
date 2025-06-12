# Stage 2:

In this stage we will focus on setting up the `Dockerfile` with the necessary steps to build and package the application.

**Reminder:** 

This project will create a custom image that runs a simple Flask application. The application is already present in the `hyper-app` directory in your project directory.

## Objectives

- Build your image from `python:3.11-slim`;
- Expose port `8000`;
- Define the working directory `/home/app`;
- Add the content of the `hyper-app` to the working directory;
- Add a run instruction with `pip install -r requirements.txt` to the `Dockerfile` to install the project dependencies.
- Make the entrypoint of the image, run the following command with parameters `["python3", "main.py"]`.

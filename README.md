## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Usage](#usage)
- [CI/CD and Cloud Deployment](#cicd-and-cloud-deployment)
- [Contributing](#contributing)

## Project Description

Celebrity Image Detector is a cloud-powered application that recognizes celebrities in images using AI and computer vision. Leveraging Groq for fast LLM inference, OpenCV for efficient image analysis, and a Flask backend with a simple HTML/CSS user interface, this app offers seamless live deployment via Docker on Google Kubernetes Engine (GKE). With CircleCI and GitHub integration, it ensures continuous delivery and scalability for real-time image recognition.

***

## Key Features

- **Celebrity Recognition:** Instantly identifies celebrities in user-uploaded images using Groq LLM and deep vision models.  
- **Real-Time Processing:** Fast image analysis and inference with OpenCV and a Flask API.  
- **Modern DevOps:** Automated build, test, and deployment using GitHub as SCM and CircleCI for CI/CD.  
- **Cloud-Native Deployment:** Containerized with Docker, stored in GCP Artifact Registry, and orchestrated on GKE Kubernetes clusters.  
- **Web UI:** Simple and intuitive HTML/CSS frontend for easy image uploads and results visualization.  
- **Scalable & Portable:** Deployable locally or in the cloud for different team and user needs.

***

## Tech Stack

- **Groq**: Fast and efficient LLM for image-to-identity recognition.
- **OpenCV (Python)**: Image detection and preprocessing.
- **Flask**: Backend REST API server.
- **HTML/CSS**: Frontend user interface.
- **Docker**: Containerization for local and cloud deployments.
- **CircleCI**: CI/CD pipeline for automated testing and deployment.
- **GitHub**: Source code management and collaboration.
- **GCP GAR**: Artifact repository for storing Docker images.
- **GCP GKE**: Deployment and orchestration on Kubernetes.

***

## Architecture

```
[HTML/CSS UI] <---> [Flask REST API] <---> [Groq LLM] + [OpenCV]
        ↑
        |
[Docker Container]
        |
[GitHub → CircleCI → GAR → GKE]
```

- Frontend allows image uploads via a simple browser interface.
- Flask backend receives images, applies OpenCV for preprocessing, and interacts with Groq LLM for celebrity recognition.
- CircleCI automates testing and Docker builds; images pushed to Google Artifact Registry.
- GKE orchestrates containers for robust cloud service.

***

## Usage

- Access the UI at `http://localhost:5000` after start.
- Upload any image containing a celebrity.
- App returns the identified celebrity name and confidence score.

***

## CI/CD and Cloud Deployment

- Source pushed to **GitHub** triggers CircleCI pipeline.
- **CircleCI**: Lints code, runs tests, builds Docker image.
- **Docker image** uploaded to **GCP GAR**.
- On success, **CircleCI** updates container on **GCP GKE** seamlessly.

***

## Contributing

1. Fork the repo on GitHub.
2. Create a branch for your feature or bugfix.
3. Submit a pull request.
4. All code is automatically tested via CircleCI.

***

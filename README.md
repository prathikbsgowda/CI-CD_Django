#  CI/CD Django Project

This is a sample Django project demonstrating **CI/CD using Docker and GitHub Actions**.

---

##  Features

- Django web app
- Dockerized environment
- GitHub Actions for:
  - Running tests
  - Building Docker image
  - Pushing to Docker Hub

---

##  Tech Stack

- Python 3.10
- Django 4.x
- Docker
- GitHub Actions

---

## 📁 Project Structure

```
.
├── demo_project/        # Django project
├── web/                 # Django app
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── manage.py
└── .github/workflows/ci-cd.yml
```


##  CI/CD Pipeline (GitHub Actions)

On every push to `main`:
1. Install dependencies
2. Run Django tests
3. Build Docker image
4. Push image to Docker Hub

---

##  GitHub Secrets Required

| Secret Name        | Description                      |
|--------------------|----------------------------------|
| `DOCKER_USERNAME`  | Your Docker Hub username         |
| `DOCKER_PASSWORD`  | Docker Hub password or token     |

---

## 📦 DockerHub Image

> Replace this with your actual Docker Hub image link once pushed

```bash
docker pull your-username/django-ci-cd-demo
```



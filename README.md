# FastAPI User Management

This project implements a FastAPI application for user management with CRUD operations.

## Instructions for Running the Project

### Prerequisites
- Python 3.x
- Docker (optional)

### Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd fastapi-user-management
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Running the FastAPI Server:
```bash
python3 main.py
```
4. Running Tests
```bash
pytest
```

### Docker Setup and Usage (optional)

1. Build the Docker image:
```bash
docker build -t fastapi-user-management .
```
2. Run the Docker container:
```bash
docker run -d -p 8000:8000 fastapi-user-management
```
### API Documentation
```bash
http://localhost:8000/docs
```
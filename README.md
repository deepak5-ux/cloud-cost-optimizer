# Cloud Cost Optimizer API

An intelligent and scalable **AI-powered Cloud Cost Optimizer API** built with **FastAPI**, trained using both real and synthetic data, designed to recommend the most optimal AWS cloud resources based on **user workloads, budget, and usage pattern**. This project showcases practical implementation of **Machine Learning**, **MLOps**, **Docker**, and **API key-based security**, aimed to highlight skills relevant to modern backend and DevOps roles.

---

## 🚀 Features

- 🔍 Intelligent resource recommendation (EC2 instance type, storage, etc.)
- 📊 Trained ML model with EDA and rule-based fallback
- 🔐 API Key authentication using `.env`
- 🧪 Modularized codebase with separation of concerns
- 📦 Dockerized for seamless deployment
- ⚙️ Ready for deployment on Render, AWS EC2, or any container service
- 🧠 Designed to showcase MLOps and API development capabilities

---

## 📁 Project Structure

```
cloud-resource-recommender/
│
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── predictor.py         # ML-based prediction logic
│   ├── rule_based.py        # Fallback logic for unknown input
│   └── input_schema.py      # Request data validation with Pydantic
│
├── dataset/                 # Training datasets (real + synthetic)
│
├── models/                  # Saved ML model (.pkl or .joblib)
│
├── notebooks/               # EDA, preprocessing, training notebooks
│
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker image config
├── .dockerignore            # Ignored files during Docker build
├── .env                     # API Key and environment config
└── README.md
```

---

## 🧠 How It Works

1. **Preprocessing & Training** done in Jupyter notebooks:
   - EDA, feature engineering, and model training
   - Trained model saved to `models/`

2. **API Layer (FastAPI)**:
   - Receives JSON input with workload requirements
   - Validates via Pydantic schema
   - Predicts optimal resource or falls back to rule-based logic

3. **Security**:
   - Requires `API_KEY` as header: `X-API-Key`

4. **Deployment**:
   - Fully Dockerized: `docker build` + `docker run`
   - Easily deployable to any cloud

---

## 🔑 API Usage (via Swagger)

After running the container:

```
http://localhost:8000/docs
```

### Example Request:
**Header**:
```
X-API-Key: your_api_key_here
```

**Body**:
```json
{
  "cpu": 4,
  "memory": 16,
  "storage": 100,
  "workload_type": "machine_learning",
  "budget": 150
}
```

**Response**:
```json
{
  "recommended_instance": "t3.large",
  "estimated_cost": 145,
  "confidence": 0.87
}
```

---

## 🐳 Docker Instructions

### Build the Docker image
```bash
docker build -t cloud-cost-optimizer-api .
```

### Run the container
```bash
docker run -d -p 8000:8000 --env API_KEY=your_api_key cloud-cost-optimizer-api
```

---

## ✅ Requirements

```
fastapi
uvicorn
scikit-learn
pydantic
python-dotenv
joblib
numpy
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 📈 Designed for Real-World Deployment and Use

- Shows end-to-end understanding of **ML lifecycle**
- Demonstrates practical **FastAPI** + **Docker** use
- Clean structure, good code practices, security-ready
- Deployable and scalable — fits real-world developer expectations

> This project is tailored to showcase backend development, MLOps, and DevOps skills — emphasizing cloud efficiency, automation, and innovation in modern software solutions.

---

## 📌 Future Enhancements

- Add CI/CD with GitHub Actions
- Integrate with AWS Pricing APIs for real-time pricing
- Build optional front-end dashboard (React/Vite)
- Log requests and usage analytics (Prometheus/Grafana)

---

## 🤝 Contributions
This is an individual academic + placement showcase project. For feedback, open issues or connect with me!

---

## 🧠 Contact & Portfolio

- GitHub: [https://github.com/deepak5-ux]
- Docker Hub: [https://hub.docker.com/repositories/deepakb05]
- LinkedIn: [www.linkedin.com/in/deepak511]
- Mail: [deepakbalraj511@gmail.com]

---

> "Optimizing the cloud, one API call at a time."


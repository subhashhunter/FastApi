
This repository contains the backend service built with **FastAPI** for the Lexi assignment.

---

## 🚀 Features

* FastAPI-based backend
* Modular routes (`cases`, `metadata`)
* Easy deployment on Render
* Environment variable support for dynamic port assignment

---



## 🛠️ Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/subhashhunter/FastApi
cd lexi-assignment
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run locally

```bash
uvicorn app.main:app --reload
```

Your app will be running at 👉 `http://127.0.0.1:8000`

---


## 📌 API Endpoints

* **Root** → `GET /`
  Returns: `{ "message": "FastAPI server is running!" }`

* **Metadata Routes** → `GET /metadata/...`

* **Cases Routes** → `GET /cases/...`

---

## ✅ Requirements

* Python 3.9+
* FastAPI
* Uvicorn

Install everything via:

```bash
pip install -r requirements.txt
```

---


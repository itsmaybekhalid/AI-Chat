# 🚀 LLM API with Mistral, FastAPI & ngrok

A simple project that demonstrates how to serve a Large Language Model (LLM) through a REST API using **FastAPI**, expose the local API using **ngrok**, and consume it from an external client or GUI.

This project was developed as part of the **Tips Hindawi Internship**.

---

## 📌 Project Overview

The main goal of this project is to transform a locally running LLM into an API that can be accessed by external applications.

The project uses **Mistral-Nemo-Instruct-2407** for text generation and exposes it through a FastAPI endpoint.

The overall workflow is:

```text
Client / Streamlit
        ↓
   HTTP Request
        ↓
     ngrok
        ↓
    FastAPI API
        ↓
 Mistral-Nemo-Instruct-2407
        ↓
 Generated Response
```

---

## ✨ Features

- 🤖 Run **Mistral-Nemo-Instruct-2407** locally
- ⚡ Build a REST API using **FastAPI**
- 🔐 Protect the API using **Bearer Token Authentication**
- 🌐 Expose the local API using **ngrok**
- 🐍 Python-based implementation
- 🔌 Allow external applications to communicate with the LLM
- 🖥️ Can be connected to a **Streamlit GUI**

---

## 🛠️ Tech Stack

| Technology                 | Purpose                              |
| -------------------------- | ------------------------------------ |
| Python                     | Main programming language            |
| PyTorch                    | Running the language model           |
| Hugging Face Transformers  | Loading and interacting with Mistral |
| Mistral-Nemo-Instruct-2407 | Text generation model                |
| FastAPI                    | Building the REST API                |
| Uvicorn                    | Running the FastAPI server           |
| pyngrok                    | Creating a public URL                |
| Streamlit                  | Optional GUI / external client       |

---

## 📂 Project Structure

```text
.
├── notebook.ipynb
├── streamlit_app.py
├── README.md
└── requirements.txt
```

> The exact structure may vary depending on how the project is organized.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn pyngrok transformers==4.52.4 accelerate torch streamlit requests
```

Or, if a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure ngrok

Create an account on ngrok and get your authentication token.

Then replace:

```python
NGROK_TOKEN = "ADD_NGROK_TOKEN"
```

with your actual token.

For security, **do not upload your real ngrok token or API key to GitHub**.

---

## 🔐 API Authentication

The API uses Bearer Token Authentication.

The API key is configured as:

```python
API_KEY = "secret123"
```

The client must include the following header:

```text
Authorization: Bearer secret123
```

For a real deployment, the API key should be stored in an environment variable instead of being written directly in the code.

---

## 🚀 Running the API

After loading the model, the application creates a FastAPI server and exposes the `/generate` endpoint.

Example request:

```python
import requests

URL = "YOUR_NGROK_URL/generate"

headers = {
    "Authorization": "Bearer secret123"
}

payload = {
    "prompt": "Who is Lionel Messi?",
    "max_length": 200
}

response = requests.post(
    URL,
    headers=headers,
    json=payload
)

print(response.json()["response"])
```

---

## 📡 API Endpoint

### `POST /generate`

Generates a response from the Mistral model.

### Request Headers

```text
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### Request Body

```json
{
  "prompt": "Explain Artificial Intelligence in simple terms.",
  "max_length": 200
}
```

### Example Response

```json
{
  "response": "Artificial Intelligence is a field of computer science..."
}
```

---

## ❌ Unauthorized Request

If the API key is missing or incorrect, the API returns:

```json
{
  "detail": "Unauthorized"
}
```

with HTTP status code:

```text
401 Unauthorized
```

---

## 🖥️ Streamlit Integration

The API can be consumed by a Streamlit application to provide a simple graphical interface.

The Streamlit application sends the user's prompt to the public FastAPI endpoint through an HTTP request.

```text
User
 ↓
Streamlit GUI
 ↓
Requests
 ↓
ngrok Public URL
 ↓
FastAPI
 ↓
Mistral LLM
 ↓
Response
 ↓
Streamlit GUI
```

---

## 🔒 Security Notes

This project is intended mainly for learning and demonstration purposes.

Before deploying it in a production environment:

- Store API keys in environment variables.
- Never commit secrets to GitHub.
- Use HTTPS.
- Add proper rate limiting.
- Validate incoming requests.
- Add logging and monitoring.
- Consider using a dedicated server or cloud infrastructure instead of exposing a local machine through ngrok.

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Working with Hugging Face LLMs
- Loading and running Mistral models
- Building REST APIs with FastAPI
- Handling HTTP requests and JSON data
- Implementing API authentication
- Using ngrok to expose local services
- Connecting AI models with external applications
- Integrating an LLM API with a Streamlit interface

---

## 👨‍💻 Internship

This project was developed as part of the **Tips Hindawi Internship**, where I worked on practical applications involving AI, APIs, and Large Language Models.

---

## 📌 Future Improvements

Some possible improvements include:

- Add conversation history
- Add streaming responses
- Improve error handling
- Add request validation with Pydantic
- Move secrets to `.env`
- Add Docker support
- Deploy the API to a cloud platform
- Add monitoring and logging
- Implement rate limiting

---

## ⭐ Acknowledgment

Thanks to **Tips Hindawi** for the internship experience and the opportunity to work on practical AI projects.

---

## 📄 License

This project is for educational and internship purposes.

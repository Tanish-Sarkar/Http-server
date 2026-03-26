# 🐍 Python Mini HTTP Server

![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)
![Architecture](https://img.shields.io/badge/architecture-OOP%20Handler-orange.svg)

A lightweight, high-performance HTTP server built entirely from scratch using the **Python 3.13 Standard Library**. 

This project demonstrates a clean separation of concerns (routing vs. server execution) using the Object-Oriented Handler pattern, completely avoiding the need for heavy external frameworks like Flask or FastAPI.

## ✨ Features
* **Zero External Dependencies:** Runs pure standard library code (`http.server`).
* **Clean Architecture:** Logic and routing (`app.py`) are strictly separated from server initialization (`server.py`).
* **RESTful Capabilities:** Handles both `GET` requests (serving HTML/JSON) and `POST` requests (processing incoming payloads).
* **Environment Ready:** Designed to run cleanly inside a standard Python virtual environment (`venv`).

---

## 📂 Project Structure

```text
mini_server/
├── app.py              # Application logic, routing, and HTTP handlers
├── server.py           # Server initialization, port binding, and execution
├── requirements.txt    # Documentation of zero-dependency architecture
└── README.md           # Project documentation
````

-----

## 🚀 Getting Started

### 1\. Prerequisites

Ensure you have Python 3.13+ installed on your system.

### 2\. Setup

It is best practice to run Python projects inside a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

*(Note: Because this project uses only the standard library, `pip install -r requirements.txt` is not required, but the file is included to strictly define the zero-dependency environment.)*

### 3\. Run the Server

Start the server by executing the engine script:

```bash
python server.py
```

You should see output confirming the server is running on `http://localhost:8000`.

-----

## 📡 API Endpoints & Testing

Once the server is running, you can interact with the following endpoints:

| Method | Endpoint | Description | Response Type |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Returns the application home page. | `text/html` |
| `GET` | `/api/status` | Returns a health check JSON payload. | `application/json` |
| `POST` | `/submit` | Accepts data and returns a confirmation payload. | `application/json` |

### Testing via Browser

Open your favorite web browser and navigate to:

  * **Home:** [http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)
  * **API Status:** [http://localhost:8000/api/status](https://www.google.com/search?q=http://localhost:8000/api/status)

### Testing via Terminal (cURL)

To test the POST route and ensure the server correctly handles incoming data, open a new terminal tab and run:

```bash
curl -X POST http://localhost:8000/submit \
     -H "Content-Type: application/json" \
     -d '{"name": "Test User", "project": "Mini Server"}'
```

**Expected Output:**

```json
{"message": "Data received successfully!", "data_received": "{\"name\": \"Test User\", \"project\": \"Mini Server\"}"}
```

-----

## 🛑 Shutting Down

To gracefully shut down the server, simply press `Ctrl + C` in the terminal where the server is running.


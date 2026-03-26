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
A real-time **Weather Data Streaming Application** built using **Apache Kafka, Python, PostgreSQL, and Docker**.  
The system fetches live weather data from a public API, streams it through Kafka, and stores it in a database.

---

## 🚀 Features

- Real-time weather data ingestion
- Kafka Producer–Consumer architecture
- PostgreSQL data persistence
- Fully Dockerized (one-command setup)
- Scalable event-driven design

---

## 🏗️ Architecture

Weather API → Kafka Producer → Kafka Topic → Kafka Consumer → PostgreSQL


---

## 🛠️ Tech Stack

- Python
- Apache Kafka
- PostgreSQL
- Docker & Docker Compose
- Open-Meteo API

---

## 📂 Project Structure

.
├── docker-compose.yml
├── Dockerfile
├── requirement.txt
├── weather_producer.py
├── weather_consumer.py
└── README.md


---

## ⚙️ Setup & Run

### Prerequisites
- Docker
- Docker Compose

### Run the project
```bash
docker-compose up --build
📡 Producer
Fetches live weather data every 10 seconds

Sends data to Kafka topic: weather-topic

Sample message:

{
  "time": "2026-01-22T10:30",
  "temperature": 30.1,
  "windspeed": 5.6
}
🧩 Consumer
Listens to weather-topic

Stores data in PostgreSQL table weather_data

Schema:

CREATE TABLE weather_data (
  time TEXT,
  temperature FLOAT,
  windspeed FLOAT
);
🗄️ Verify Data
docker exec -it postgres psql -U user -d weatherdb
SELECT * FROM weather_data;
🐳 Docker Services
Service	Purpose
Zookeeper	Kafka coordination
Kafka	Message broker
Producer	Weather data sender
Consumer	Data processor
PostgreSQL	Data storage
❗ Common Issues
Port / Container Conflict

docker-compose down -v
Consumer not receiving data

Ensure Kafka is running

Restart containers

🌱 Future Improvements
Multi-city weather streaming

Schema validation (Avro/JSON)

Monitoring with Grafana

Spark-based analytics

👤 Author
Makeshwaran U

⭐ Star this repo if you find it useful!


---

### ✅ Why this is perfect for GitHub
✔ Clean formatting  
✔ No unnecessary text  
✔ Easy to read on GitHub UI  
✔ Recruiter & evaluator friendly  

If you want:
- **Badges (Docker, Kafka, Python)**
- **Screenshots section**
- **License file**
- **GitHub Actions CI**

Tell me and I’ll add it 🔥
You said:
in single file
ChatGPT said:
Got it 👍
Here is the ENTIRE README.md in ONE SINGLE FILE, ready to upload directly to GitHub.

👉 Just copy everything below and paste it into README.md

# Kafka Weather Data Streaming Pipeline 🌦️

A real-time **Weather Data Streaming Application** built using **Apache Kafka, Python, PostgreSQL, and Docker**.  
This project demonstrates an **event-driven architecture** where live weather data is streamed, processed, and stored efficiently.

---

## 🚀 Features

- Real-time weather data ingestion
- Kafka Producer–Consumer architecture
- PostgreSQL data persistence
- Fully Dockerized (single command execution)
- Scalable and modular design

---

## 🏗️ System Architecture

Weather API
↓
Kafka Producer
↓
Kafka Topic (weather-topic)
↓
Kafka Consumer
↓
PostgreSQL Database


---

## 🛠️ Technology Stack

- **Python**
- **Apache Kafka**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Open-Meteo Weather API**

---

## 📂 Project Structure

Kafka-Weather-API/
│
├── docker-compose.yml
├── Dockerfile
├── requirement.txt
├── weather_producer.py
├── weather_consumer.py
└── README.md


---

## ⚙️ Prerequisites

Ensure the following are installed:

- Docker
- Docker Compose

Verify installation:
```bash
docker --version
docker-compose --version
▶️ How to Run the Project
Step 1: Clone the Repository
git clone <your-github-repo-url>
cd Kafka-Weather-API
Step 2: Start the Application
docker-compose up --build
This command starts:

Zookeeper

Kafka Broker

PostgreSQL

Kafka Producer

Kafka Consumer

📡 Kafka Producer (weather_producer.py)
Fetches real-time weather data every 10 seconds

Uses Open-Meteo API

Publishes messages to Kafka topic weather-topic

Sample message:

{
  "time": "2026-01-22T10:30",
  "temperature": 30.1,
  "windspeed": 5.6
}
🧩 Kafka Consumer (weather_consumer.py)
Subscribes to weather-topic

Reads messages from Kafka

Inserts records into PostgreSQL table weather_data

Database schema:

CREATE TABLE weather_data (
    time TEXT,
    temperature FLOAT,
    windspeed FLOAT
);
🗄️ Verify Stored Data
Access PostgreSQL container:

docker exec -it postgres psql -U user -d weatherdb
Run query:

SELECT * FROM weather_data;

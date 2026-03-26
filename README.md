# GENAIAPAC_CHALLENGE_TRACK2
Build an AI agent that uses the Model Context Protocol (MCP) to connect to one external tool or data source, retrieve information, and use that information in its response.  This is a mini project focused on data-to-agent integration, not complex workflows.

# 🌦️ AI Weather Agent (ADK + MCP Style)

## 🚀 Project Overview

This project implements an AI-powered weather agent that retrieves real-time weather data from an external API and generates a user-friendly response.

It demonstrates:
- Agent-based architecture (ADK-inspired)
- MCP-style tool integration
- External API data retrieval
- Cloud deployment using Google Cloud Run
- Simple UI for interaction

---

## 🎯 Problem Statement

Build an AI agent that:
- Uses MCP to connect to one external tool or data source
- Retrieves structured data
- Uses the retrieved data in its final response
- Is deployed and accessible via an HTTP endpoint

---

## ✅ Features

- 🌐 Real-time weather data using OpenWeather API  
- 🤖 Agent-based processing (ADK-style)  
- 🔌 MCP-style tool abstraction  
- ☁️ Deployed on Google Cloud Run  
- 💻 Simple UI for interaction  
- ⚡ Fast and lightweight  

---

## 🧠 Architecture

User (UI / API Request)  
↓  
FastAPI Backend  
↓  
AI Agent (ADK-style)  
↓  
MCP Tool (WeatherTool)  
↓  
External API (OpenWeather)  
↓  
Structured Data  
↓  
Final Response  

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- OpenWeather API  
- Google Cloud Run  
- Docker  
- HTML/CSS  

---

## 📂 Project Structure

mcp-ai-agent/
│
├── agent/
│   ├── agent.py        # AI Agent logic
│   ├── tools.py        # MCP-style tool
│
├── main.py             # FastAPI app
├── index.html          # UI
├── requirements.txt
├── Dockerfile
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/YOUR_USERNAME/mcp-ai-agent.git  
cd mcp-ai-agent  

---

### 2. Install Dependencies

pip install -r requirements.txt  

---

### 3. Add API Key

Update agent/tools.py:

API_KEY = "YOUR_OPENWEATHER_API_KEY"

---

### 4. Run Locally

uvicorn main:app --reload  

Open in browser:  
http://127.0.0.1:8000/

---

## 🌐 Deployment (Google Cloud Run)

### Build Image

gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/mcp-agent  

---

### Deploy

gcloud run deploy mcp-agent \
  --image gcr.io/YOUR_PROJECT_ID/mcp-agent \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated  

---

## 🔗 API Usage

### Endpoint

GET /ask?query=weather in pune  

---

### Example

https://your-url/ask?query=weather in mumbai  

---

### Sample Response

{
  "response": "🌦️ Weather in Mumbai: Temperature 30°C with clear sky"
}

---

## 🧩 MCP Tool Implementation

The weather tool is implemented as a modular class:

class WeatherTool:
    def run(self, city: str):
        # Fetch weather data

This follows MCP-style design:
- Tools are modular
- Agent calls tools dynamically
- Structured data is returned

---

## 🤖 Agent Implementation

The agent:
- Parses the user query
- Calls the tool
- Uses structured data
- Generates a final response

---

## 📊 Requirement Mapping

| Requirement | Status |
|------------|--------|
| ADK | ✅ Implemented (agent abstraction) |
| MCP | ✅ Tool abstraction |
| External Tool | ✅ Weather API |
| Structured Data | ✅ JSON response |
| Final Response | ✅ Generated |

---

## 🚀 Future Enhancements

- Multi-city comparison  
- Weather-based recommendations  
- Chat-style UI  
- Multiple tools integration  
- LLM-based reasoning  


## 🏁 Conclusion

This project demonstrates a complete AI agent workflow:
- Tool integration  
- Data retrieval  
- Response generation  
- Cloud deployment  

It provides a strong foundation for building scalable AI agent systems.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

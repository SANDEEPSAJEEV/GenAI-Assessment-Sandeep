📌 Overview

This project implements an agentic pipeline using LangGraph and LangChain with two main functionalities:
Real-time Weather Data Retrieval (via OpenWeatherMap API)
PDF-based Question Answering (RAG) using Qdrant as a vector database

It includes:

LangGraph routing logic to decide between weather API calls and RAG-based PDF retrieval.
Embedding generation and vector storage in Qdrant.
LLM-powered processing using Groq Gemma-7B-IT.
Evaluation with LangSmith.
A Streamlit UI for interactive demonstration.
Unit tests for API handling, LLM processing, and routing.
Note: Due to payment restrictions, the OpenWeatherMap API key is not set in this repository. Weather functionality will require you to add a valid API key in .env.

🛠 Tech Stack
LangGraph
LangChain
Groq (gemma-7b-it model)
Qdrant (Vector DB)
Streamlit (UI)
PyPDF (PDF reading)
HuggingFaceEmbeddings
LangSmith (Evaluation)
OpenWeatherMap API

📂 Project Structure

GenAI-Assessment-Sandeep/
│
├── app.py                 # Main application (LangGraph pipeline)
├── ui.py                  # Streamlit UI
├── test_app.py            # Unit tests
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys, DB URLs)
├── Readme.md              # Project documentation
├── Sandeep_S_Resume_AI_ML_2025.pdf  # Example PDF for RAG
├── genai/                 # Supporting modules
└── __pycache__/           # Compiled files

⚙️ Setup Instructions
1️⃣ Clone the repository

git clone https://github.com/SANDEEPSAJEEV/GenAI-Assessment-Sandeep.git
cd GenAI-Assessment-Sandeep

2️⃣ Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Configure environment variables
Create a .env file:


GROQ_API_KEY=your_groq_api_key
OPENWEATHERMAP_API_KEY=your_weather_api_key  # Optional (Weather feature)
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your_qdrant_api_key
LANGSMITH_API_KEY=your_langsmith_api_key


🚀 Running the Application
1. Main Agent

python app.py

2. Streamlit UI

streamlit run ui.py

🧪 Running Tests

pytest test_app.py


📊 LangSmith Evaluation
This project uses LangSmith to evaluate LLM outputs, including accuracy and relevance for both weather queries and PDF RAG queries.
You can find evaluation logs in your LangSmith dashboard after running the application.

📌 Notes
Weather API Limitation: Weather functionality will not work until you provide a valid OpenWeatherMap API key in .env.
Large language model responses are powered by Groq’s gemma-7b-it model.
The PDF file Sandeep_S_Resume_AI_ML_2025.pdf is provided as an example for RAG.


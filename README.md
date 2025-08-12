# 🌟 GenAI Assessment – Sandeep

This repository contains a complete Generative AI application integrating **LangGraph**, **LangChain**, **Groq (Gemma-7b-it)**, **Qdrant (Vector DB)**, **Streamlit UI**, and **LangSmith** for evaluation.  
The project demonstrates Retrieval-Augmented Generation (RAG), routing, and decision-making in LangGraph nodes, along with unit tests and an interactive UI.  

> **Note:** Due to OpenWeatherMap API payment restrictions, the `OPENWEATHERMAP_API_KEY` is **not set** in this repository. Weather functionality will not work unless a valid API key is added in `.env`.

---

## 🚀 Tech Stack
- **LangGraph**
- **LangChain**
- **Groq** (`gemma-7b-it` model)
- **HuggingFaceEmbeddings**
- **Qdrant** (Vector DB)
- **Streamlit** (UI)
- **PyPDF** (PDF parsing)
- **LangSmith** (Evaluation)
- **OpenWeatherMap API** (Weather feature – optional)

---

## 📂 Project Structure

GenAI-Assessment-Sandeep/
│── app.py # Main application (LangGraph pipeline)
│── ui.py # Streamlit UI
│── test_app.py # Unit tests
│── requirements.txt # Python dependencies
│── .env # Environment variables
│── Readme.md # Project documentation
│── Sandeep_S_Resume_AI_ML_2025.pdf # Example resume for RAG
│── genai/ # Supporting modules
│── pycache/ # Compiled files



---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SANDEEPSAJEEV/GenAI-Assessment-Sandeep.git
cd GenAI-Assessment-Sandeep


# On Mac/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt


4️⃣ Configure environment variables
Create a .env file:

GROQ_API_KEY=your_groq_api_key
OPENWEATHERMAP_API_KEY=your_weather_api_key    # Optional (Weather feature)
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your_qdrant_api_key
LANGSMITH_API_KEY=your_langsmith_api_key

▶️ Running the Application
Run Streamlit UI
streamlit run ui.py

🧪 Testing
Run unit tests:
pytest test_app.py




📊 LangSmith Evaluation
Logged LLM responses with LangSmith.
Evaluated decision-making correctness within LangGraph.
Screenshots of LangSmith results are included in the report.

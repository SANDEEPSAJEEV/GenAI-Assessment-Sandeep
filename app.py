import os
import requests
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Qdrant
from langgraph.graph import StateGraph, END

# Load environment variables
load_dotenv()

# LangSmith observability
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING", "true")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT", "https://api.smith.langchain.com")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT", "ai-assignment")

# Initialize LLM (Groq - Gemma-7b-it)
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="gemma2-9b-it",
    temperature=0
)

# Prepare vector DB
def init_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    loader = PyPDFLoader("Sandeep_S_Resume_AI_ML_2025.pdf")
    docs = loader.load()
    qdrant = Qdrant.from_documents(
        docs,
        embeddings,
        location=":memory:",  # In-memory for demo
        collection_name="pdf_docs"
    )
    return qdrant

vectorstore = init_vectorstore()

# Weather API
def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    if "main" in data:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"Weather in {city}: {temp}°C, {desc}"
    return f"Weather data for '{city}' not found."

# Decide route
def decide_node(state):
    query = state["query"].lower()
    if "weather" in query:
        return "weather"
    return "rag"

# Weather node
def weather_node(state):
    return {"result": get_weather(state["query"].split("in")[-1].strip())}

# RAG node
def rag_node(state):
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )
    answer = qa.run(state["query"])
    return {"result": answer}

# Build LangGraph
graph = StateGraph(dict)

graph.add_node("weather", weather_node)
graph.add_node("rag", rag_node)
graph.set_entry_point("router")

graph.add_conditional_edges("router", decide_node, {
    "weather": "weather",
    "rag": "rag"
})
graph.add_edge("weather", END)
graph.add_edge("rag", END)

# Router function
def router_node(state):
    return state

graph.add_node("router", router_node)
app_graph = graph.compile()

if __name__ == "__main__":
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            break
        result = app_graph.invoke({"query": user_query})
        print("Bot:", result["result"])

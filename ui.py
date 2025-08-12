import streamlit as st
from app import app_graph

st.title("AI Assignment Demo")
st.write("Ask about weather or PDF content.")

query = st.text_input("Enter your question:")

if query:
    result = app_graph.invoke({"query": query})
    st.success(result["result"])

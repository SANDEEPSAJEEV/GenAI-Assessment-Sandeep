import pytest
from unittest.mock import patch, MagicMock
import app

def test_decide_node_weather():
    assert app.decide_node({"query": "What's the weather in Paris?"}) == "weather"

def test_decide_node_rag():
    assert app.decide_node({"query": "Tell me about chapter 1"}) == "rag"

@patch("app.requests.get")
def test_get_weather_success(mock_get):
    mock_get.return_value.json.return_value = {
        "main": {"temp": 22},
        "weather": [{"description": "clear sky"}]
    }
    res = app.get_weather("Paris")
    assert "22" in res and "clear sky" in res

@patch("app.requests.get")
def test_get_weather_fail(mock_get):
    mock_get.return_value.json.return_value = {}
    res = app.get_weather("Nowhere")
    assert "not found" in res.lower()

@patch("app.RetrievalQA.from_chain_type")
def test_rag_node(mock_rag):
    mock_instance = MagicMock()
    mock_instance.run.return_value = "Mock PDF Answer"
    mock_rag.return_value = mock_instance
    res = app.rag_node({"query": "PDF question"})
    assert "Mock PDF Answer" in res["result"]

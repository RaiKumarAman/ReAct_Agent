# tools.py
import requests
from langchain.tools import tool
from ddgs import DDGS
import os
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()


class WebSearchInput(BaseModel):
    query: str = Field(description="Search query text only")


@tool("web_search")
def web_search(query: str) -> str:
    """Search the web for recent information using a query string."""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(f"{r['title']} - {r['body']} ({r['href']})")
 
    return "\n".join(results)
    # return ddgs.text(query, max_results=5)


@tool("get_weather")
def get_weather(city: str) -> str:
    """Get current weather for a given city."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url, timeout=10).json()

    if response.get("cod") != 200:
        return "Weather data not available."

    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]

    return f"{city}: {temp}°C, {desc}"

# response= get_weather.invoke({"city": "Hyderabad"})
# response = web_search.invoke({"query": "who is SRK"})
# print(response)
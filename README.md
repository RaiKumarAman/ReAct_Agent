# ReAct AI Assistant 🤖
An autonomous AI agent implementation built using LangChain, Groq, and the ReAct (Reasoning + Acting) framework. This assistant intelligently decides when to use external tools—specifically DuckDuckGo Search and OpenWeatherMap—to provide grounded, real-time responses to user queries.

### 🚀 Features

1. Intelligent Reasoning: Leverages the meta-llama/llama-4-maverick-17b model via Groq for low-latency, high-logic reasoning.


2. Autonomous Tool Selection: Automatically chooses between web_search for facts and get_weather for climate data based on user intent.


3. Live Research: Integrated with DuckDuckGo (via ddgs) to summarize web findings without listing cluttered links.


4. Clean Output: Optimized system instructions ensure the agent provides final answers in plain natural language, hiding internal reasoning and tool metadata from the user.


5. Tool Trace Monitoring: The CLI interface includes a detector that explicitly highlights when a tool is being called and what data is being retrieved.

### 📁 Project Structure

agent.py: Configures the ChatGroq model and the ReAct agent logic.


tools.py: Contains the technical implementation of the web_search and get_weather functions using Pydantic for input validation.


main.py: The interactive command-line interface with built-in tool-usage tracing.


requirements.txt: List of dependencies including langchain-groq, ddgs, and python-dotenv.

### 🛠️ Setup & Installation
1. Clone the Repository
Bash
git clone https://github.com/your-username/react-ai-agent.git
cd react-ai-agent
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configuration
Create a .env file in the root directory and add your API keys:

Code snippet
GROQ_API_KEY='your_groq_api_key'
OPENWEATHER_API_KEY='your_openweather_api_key'
💻 Usage
Run the agent via the interactive CLI:

Bash
python main.py
Example Interaction
User: "What is the current temperature in London and who is the current Prime Minister?"

### AI Agent Output:

🤖: Calls Weather Tool → gets data
🤖: Calls Web Search Tool → summarizes data

The current temperature in London is 14°C with light rain. The current Prime Minister of the United Kingdom is [Name].

### ⚙️ Technical Details

1. Logic Engine: LLaMA-4-Maverick-17B.


2. Temperature: 0 (Optimized for factual accuracy and consistency).


3. Search: Scrapes top 5 results from DuckDuckGo for context synthesis.


4. Weather: Pulls metric units (Celsius) from the OpenWeatherMap API.

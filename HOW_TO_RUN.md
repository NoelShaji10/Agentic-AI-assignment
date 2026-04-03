# Autonomous Research Agent

This is an autonomous research agent built using LangChain, LangGraph, and the Groq API. It can search the web (DuckDuckGo) and Wikipedia to compile structured Markdown reports on any given topic.

## Prerequisites

1. Python 3.8+ installed on your system.
2. A free API key from [Groq](https://console.groq.com/).

## Setup Instructions

**1. Clone or download the repository** (navigate to the project folder)
```bash
cd "Agentic AI"
```

**2. (Optional but recommended) Create and activate a virtual environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install the required dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up the environment variables**
Create a file named `.env` in the root of the project directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## How to Run

You can run the script from the terminal and provide an optional research topic.

**Basic Usage:**
If you don't provide a topic, it will default to researching "Impact of AI in Healthcare".
```bash
python agent.py
```

**Custom Topic:**
Provide a topic surrounded by quotes:
```bash
python agent.py "Quantum Computing"
```

The agent will begin researching the topic, and once completed, it will:
1. Print the final report in the terminal.
2. Save a Markdown file containing the report in the current directory (e.g., `quantum_computing_report.md`).

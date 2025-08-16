
# 🤖 Agents Collection

A collection of mini AI agents built using **LiteLLM** with **Groq's free models**.

## Agents included
- **Math Agent** → solves `+ - * /` only. Anything else => `Invalid expression`.
- **Quiz Agent** → generates a multiple-choice question (A–D) and checks your answer locally.
- **Tutor Agent** → explains any concept simply (like teaching a 10-year-old)


## Requirements
- Python 3.9+ recommended
- A Groq API key

## Install
```bash
pip install -r requirements.txt
```
(Or in Colab:)
```bash
!pip install -r requirements.txt
```

## Set API Key
Export your Groq key so LiteLLM can pick it up.
```bash
# macOS/Linux
export GROQ_API_KEY="your_api_key_here"

# Windows (PowerShell)
setx GROQ_API_KEY "your_api_key_here"
```
> Restart your shell after `setx` on Windows or run `refreshenv` if you use Chocolatey.

In Google Colab you can do:
```python
import os
os.environ["GROQ_API_KEY"] = "your_api_key_here"
```

## Run
From the project root:
```bash
python run_agent.py math
# or
python run_agent.py quiz
```

### Example (Math Agent)
```
Math Agent ready! Type 'exit' to stop.
You: 20 + 2
Agent: 22
You: 87 % 4
Agent: Invalid expression
```

### Example (Quiz Agent)
```
Quiz Agent ready! Type 'ask' to get a question, then answer with A/B/C/D. Type 'skip' for a new one, 'exit' to quit.
You: ask
Q: What is the capital of France?
A) Berlin
B) Madrid
C) Paris
D) Rome
You: C
✅ Correct! C
(Explanation...) 
```

## Project Structure
```
agents-collection/
├─ agents/
│  ├─ math_agent.py
│  ├─ quiz_agent.py
│  └─ tutor_agent.py
│  
├─ run_agent.py
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## GitHub: step-by-step

1) **Create the folder locally or use this ready-made template (download below).**  
2) **Initialize Git**:
```bash
git init
git add .
git commit -m "Initial commit: agents collection (math + quiz)"
```
3) **Create a new repo on GitHub** (web UI → New → name it `agents-collection`).  
4) **Add the remote & push**:
```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/agents-collection.git
git push -u origin main
```
5) **(Optional) Try in Colab**: Upload the repo or `git clone` it, install requirements, set `GROQ_API_KEY`, and run an agent.

## Next ideas
- Keep last math result in memory (`ans`) so you can say: *"multiply that by 3"*.
- Add a web-search tool to an agent.
- Turn this into a small framework with a registry for tools.

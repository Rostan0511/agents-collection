
import sys

def run_math():
    from agents import math_agent
    math_agent.run_agent()

def run_quiz():
    from agents import quiz_agent
    quiz_agent.run_agent()

def run_tutor():
    from agents import tutor_agent
    tutor_agent.run_agent()

AGENTS = {
    "math": run_math,
    "quiz": run_quiz,
    "tutor": run_tutor,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_agent.py [agent_name]")
        print("Available agents:", ", ".join(AGENTS.keys()))
        raise SystemExit(1)

    agent_name = sys.argv[1].lower()
    if agent_name in AGENTS:
        AGENTS[agent_name]()
    else:
        print(f"Unknown agent: {agent_name}")
        print("Available agents:", ", ".join(AGENTS.keys()))

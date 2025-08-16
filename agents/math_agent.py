
import os
from typing import List, Dict
from litellm import completion

# LiteLLM will read GROQ_API_KEY from your environment

def generate_response(messages: List[Dict]) -> str:
    response = completion(
        model="groq/llama-3.1-8b-instant",
        messages=messages,
        max_tokens=256
    )
    return response.choices[0].message["content"]

# ---- Math Agent ----
messages = [
    {
        "role": "system",
        "content": (
            "You are a math agent. "
            "You can ONLY solve expressions with + - * /. "
            "If the user provides such an expression, calculate and return ONLY the final answer (no steps). "
            "If the input is anything else, reply exactly: 'Invalid expression'."
        ),
    }
]

def run_agent():
    print("Math Agent ready! Type 'exit' to stop.")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})
        reply = generate_response(messages)
        print("Agent:", reply)
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    run_agent()

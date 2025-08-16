from typing import List, Dict
from litellm import completion

def generate_response(messages: List[Dict]) -> str:
    response = completion(
        model="groq/llama-3.1-8b-instant",
        messages=messages,
        max_tokens=400
    )
    return response.choices[0].message["content"]

# ---- Tutor Agent ----
messages = [
    {
        "role": "system",
        "content": (
            "You are a tutor who explains things in the simplest way possible. "
            "Use short sentences, simple words, and examples when needed. "
            "Imagine you are teaching a 10-year-old."
        ),
    }
]

def run_agent():
    print("Tutor Agent ready! Type 'exit' to stop.")
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

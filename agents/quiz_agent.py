
import json
from typing import List, Dict
from litellm import completion

def llm_generate_question(topic: str = "general knowledge") -> Dict:
    """Ask the model for a single MCQ (A–D) in strict JSON."""
    sys_prompt = {
        "role": "system",
        "content": (
            "You are a quiz generator. "
            "Return ONLY valid JSON with keys: question (string), options (array of 4 strings), "
            "answer (one of 'A','B','C','D'), explanation (string). "
            "No extra text, no code fences."
        ),
    }
    user_prompt = {
        "role": "user",
        "content": (
            f"Generate ONE multiple-choice question about '{topic}'. "
            "Ensure options length is exactly 4 and answer is one of A/B/C/D."
        ),
    }
    resp = completion(
        model="groq/llama-3.1-8b-instant",
        messages=[sys_prompt, user_prompt],
        max_tokens=400
    )
    text = resp.choices[0].message["content"]
    return json.loads(text)  # may raise if not valid JSON

def run_agent():
    print("""Quiz Agent ready! 
Type 'ask' (or 'ask <topic>') to get a question, then answer with A/B/C/D.
Type 'skip' for a new question, 'exit' to quit.""")
    current = None  # holds dict with question/options/answer/explanation

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if user_input.lower() == "exit":
            break

        if user_input.lower().startswith("ask"):
            topic = user_input[3:].strip() or "general knowledge"
            try:
                current = llm_generate_question(topic)
                # Print in friendly format
                print("Q:", current["question"])
                letters = ["A", "B", "C", "D"]
                for i, opt in enumerate(current["options"]):
                    print(f"{letters[i]}) {opt}")
            except Exception as e:
                print("Sorry, couldn't generate a question. Try again.")
                current = None
            continue

        if user_input.upper() in {"A", "B", "C", "D"}:
            if not current:
                print("No active question. Type 'ask' first.")
                continue
            if user_input.upper() == current["answer"].upper():
                print(f"\u2705 Correct! {current['answer']}")
            else:
                print(f"\u274C Incorrect. Correct answer is {current['answer']}")
            # show explanation
            expl = current.get("explanation")
            if expl:
                print(expl)
            # reset after answer
            current = None
            continue

        if user_input.lower() == "skip":
            current = None
            print("Skipped. Type 'ask' for a new question.")
            continue

        print("Commands: 'ask' (or 'ask <topic>'), then answer with A/B/C/D, 'skip', 'exit'.")

if __name__ == "__main__":
    run_agent()

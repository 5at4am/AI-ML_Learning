import requests
import json

# ==============================
# CONFIG
# ==============================
API_KEY = "AIzaSyA2YhZVnXlWZGOOnW17RPoC8-yJzYR_2JM"
MODEL = "gemini-2.5-flash"

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

HEADERS = {
    "Content-Type": "application/json"
}

# ==============================
# CORE FUNCTION
# ==============================
def ask_gemini(prompt: str) -> dict:
    """
    Sends user prompt to Gemini via REST API
    Returns JSON response
    """

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        return {
            "error": True,
            "status_code": response.status_code,
            "details": response.text
        }

    data = response.json()

    try:
        output_text = data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        output_text = None

    return {
        "error": False,
        "model": MODEL,
        "input": prompt,
        "output": output_text
    }

# ==============================
# CLI LOOP
# ==============================
def main():
    print("Gemini Console Chatbot (JSON Output)")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        result = ask_gemini(user_input)

        print("\nResponse (JSON):")
        print(json.dumps(result, indent=2))
        print("-" * 50)


if __name__ == "__main__":
    main()

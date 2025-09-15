import requests
from config import HF_API_KEY
from colorama import Fore, Style, init

init(autoreset=True)


DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(model_name):

    return f"https://api-inference.huggingface.co/models/{model_name}"

def query(payload, model_name=DEFAULT_MODEL):
    """
    Sends a POST request to the HF API using the specified model.
    """
    api_url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

def summarize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):

    payload = {
        "input": text,
        "parameters": {"min_length": min_length, "max_length": max_length}
    }

    print(Fore.BLUE + Style.BRIGHT + f"\n???? Performing AI summarization using model: {model_name}")

    result = query(payload, model_name=model_name)



    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "Error in response:", result)

if __name__ == "__main__":
    print(Fore.GREEN + Style.BRIGHT + "\n???? What's Your name?")
    user_name = input("Your name: ").strip()
    if not user_name:
        user_name = "User"
    print(Fore.GREEN + Style.BRIGHT + f"\n???? Hello, {user_name}! Let's summarize some text. Enter some text")

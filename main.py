import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

gen_model = 'gemini-2.0-flash-001' 

messages = []

def get_token_counts(prompt_text):
    messages.append(types.Content(role="user", parts=[types.Part(text=prompt_text)]))
    
    response = client.models.generate_content(model=gen_model, contents=messages)
    messages.append(response.candidates[0].content)

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    return response.text, prompt_tokens, response_tokens


def main():

    if len(sys.argv) > 1:
        is_verbose = '--verbose' in sys.argv
        filtered_args = [arg for arg in sys.argv[1:] if arg != '--verbose']
        prompt_text = " ".join(filtered_args)
        output, prompt_tokens, response_tokens = get_token_counts(prompt_text)
        if is_verbose:
            print(f"User prompt: {prompt_text}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
        else:
            print(output)
    else:
        # Run in interactive mode
        print("Interactive chat mode (type 'exit' to quit)\n")
        while True:
            prompt_text = input("You: ")
            if prompt_text.lower() in ["exit", "quit"]:
                break
            output, prompt_tokens, response_tokens = get_token_counts(prompt_text)
            print(f"Gemini: {output}")
            print(f"(Prompt tokens: {prompt_tokens}, Response tokens: {response_tokens})\n")


if __name__ == "__main__":
    main()

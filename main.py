import os 
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# content = 'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'

gen_model = 'gemini-2.0-flash-001' 

#content = 'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'

def get_token_counts(prompt_text):
    response = client.models.generate_content(model=gen_model, contents=prompt_text)
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    return response.text, prompt_tokens, response_tokens


def main():
    #prompt_text = input("Enter your prompt: ")
    if len(sys.argv) < 2:
        print("Error: No prompt provided. Please pass a prompt as a command-line argument.")
        sys.exit(1)

    # Join all arguments after the script name as the full prompt
    prompt_text = " ".join(sys.argv[1:])

    output, prompt_tokens, response_tokens = get_token_counts(prompt_text)
    print(output)
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()

import os 
import sys
from config import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.tools import available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

gen_model = 'gemini-2.0-flash-001' 

messages = []

config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
        )

def generate_agent_response(prompt_text):
    messages.append(types.Content(role="user", parts=[types.Part(text=prompt_text)]))

    response = client.models.generate_content(
        model=gen_model,
        contents=messages,
        config=config
    )
    if response.candidates and response.candidates[0].content:
        messages.append(response.candidates[0].content)
    
    return response

def get_token_counts(response):
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    return prompt_tokens, response_tokens


def main():

    if len(sys.argv) > 1:
        is_verbose = '--verbose' in sys.argv
        filtered_args = [arg for arg in sys.argv[1:] if arg != '--verbose']
        prompt_text = " ".join(filtered_args)
        response = generate_agent_response(prompt_text)
        prompt_tokens, response_tokens = get_token_counts(response)

        output = response.text
        if response.function_calls:
            for function_call in response.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")

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
            
            response = generate_agent_response(prompt_text)
            prompt_tokens, response_tokens = get_token_counts(response)
            output = response.text

            if response.function_calls:
                for function_call in response.function_calls:
                    print(f"Calling function: {function_call.name}({function_call.args})")
            print(f"gemini: {output}")
            print(f"(Prompt tokens: {prompt_tokens}, "
                  f"Response tokens: {response_tokens})\n")


if __name__ == "__main__":
    main()

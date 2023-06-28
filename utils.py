import openai

def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        max_tokens=500,
        temperature=0,
    )
    return response

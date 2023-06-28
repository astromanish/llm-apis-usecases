import openai

def generate_response(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=conversation,
        max_tokens=10,
        temperature=0,
    )
    return response.choices[0].message.content

import openai

openai.api_key = "ANOTHER"

msg = []


def get_response(message):
    message = str(message)
    msg.append({'role': "user", 'content': message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    answer = response["choices"][0]["message"]["content"]
    msg.append({'role': 'assistant', 'content': answer})
    return answer

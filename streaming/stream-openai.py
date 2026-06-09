from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': 'You are helpful AI Assistant.' },
        { 'role': 'user', 'content': 'Hello How are you?' }
    ],
    stream=True
)

# print(response.choices[0].message.content)
for event in response:
    print(event.choices[0].delta.content)
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

user_query = input("Ask anything: ")


response = client.responses.create(
    model='gpt-4o-mini',
    input=[
        { 'role': 'system', 'content': 'You are helpful AI Assistant.' },
        { 'role': 'user', 'content': user_query }
    ],
    # stream=True (for Streaming)
)

# for chunk in response:
#     print(chunk)

print(response.output_text)
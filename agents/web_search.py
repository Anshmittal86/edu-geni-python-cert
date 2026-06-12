from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    tools=[{"type": "web_search"}],
    input="What is the weather of bijnor?"
)

print(response.output_text)
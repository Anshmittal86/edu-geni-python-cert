import json
import requests

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather report.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city which user can interested to know the weather report.",
                },
            },
            "required": ["city"],
         },
    }
]

def get_weather(city: str) -> str:
    url = f'https://wttr.in/{city}?format=%C+%t'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The current weather of {city} is {response.text}"
    
    return "Something is wrong"


input_list = [
    { "role": "user", "content": "What is the weather of mumbai?" }
]

response = client.responses.create(
    model="gpt-4o-mini",
    tools=tools,
    input=input_list, 
)

input_list += response.output

for item in response.output:
    if item.type == "function_call":
        if item.name == "get_weather":
            city = json.loads(item.arguments)["city"]
            report = get_weather(city)
            
            input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": report,
            })

response = client.responses.create(
    model="gpt-5.5",
    instructions="You are helpful AI assistant. Your task is to answer user query based on available tool, if tool is not available so say 'Sorry currently tool is going at maintenance'",
    tools=tools,
    input=input_list,
)

print("Final output:")
print(response.model_dump_json(indent=2))
print("\n" + response.output_text)
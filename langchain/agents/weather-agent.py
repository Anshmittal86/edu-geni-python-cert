from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from dotenv import load_dotenv
import requests

load_dotenv()

@tool
def get_weather(city: str) -> str:
    """ Take city name as an parameter and give the latest weather report. """
    url = f'https://wttr.in/{city}?format=%C+%t'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The current weather of {city} is {response.text}"
    
    return "Something is wrong"

agent = create_agent(
    model='gpt-4o-mini',
    tools=[get_weather]
)

user_query = input("Question: ")
result = agent.invoke({
    "messages": [
        HumanMessage(user_query)
    ]
})

print(result['messages'][-1].content)
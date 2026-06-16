import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
import requests

load_dotenv()

@function_tool 
def get_weather(city: str) -> str:
    url = f'https://wttr.in/{city}?format=%C+%t'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The current weather of {city} is {response.text}"
    
    return "Something is wrong"

agent = Agent(
    name="Weather Forecaster.",
    instructions="Act as a Weather Forecaster.",
    model="gpt-4o-mini",
    tools=[get_weather]
)

async def main() -> None:
    result = await Runner.run(agent, "What is the weather of muzaffarnagar?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
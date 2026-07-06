from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from dotenv import load_dotenv
import requests

load_dotenv()

@tool
def researcher(topic: str) -> str:
    """ Take topic as an parameter and give the latest research of the topic. """
    return "research is coming soon..."

@tool
def writer(facts: str) -> str:
    """ Take facts as an parameter and write a polished summary"""
    return "writer is coming soon..."

agent = create_agent(
    model='gpt-4o-mini',
    tools=[researcher, writer]
)

user_query = input("Question: ")
result = agent.invoke({
    "messages": [
        HumanMessage(user_query)
    ]
})

print(result['messages'][-1].content)
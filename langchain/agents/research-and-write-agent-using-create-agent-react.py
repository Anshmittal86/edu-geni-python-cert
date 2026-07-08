from langchain.agents import create_agent
from langchain.messages import HumanMessage, ToolMessage
from langchain.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=api_key)

@tool
def researcher(topic: str) -> str:
    """Take topic as an parameter and give the latest research of the topic."""
    try:
        response = tavily_client.search(topic)
    except Exception as e:
        print(f'Something is wrong: {str(e)}')
    return response

@tool
def writer(researcher_response: str) -> str:
    """ Take facts as an parameter and write a polished summary"""
    
    writer_result = agent.invoke({
        "messages": [
            ToolMessage(researcher_response)
        ]
    })
    
    return writer_result

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
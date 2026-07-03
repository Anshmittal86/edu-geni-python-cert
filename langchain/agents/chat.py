from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

agent = create_agent(model='gpt-4o-mini')

# agent.invoke('hello how are you')

user_query = input("Question: ")

result = agent.invoke({
    "messages": [
        HumanMessage(user_query)
    ]
})

print(result['messages'][-1].content)
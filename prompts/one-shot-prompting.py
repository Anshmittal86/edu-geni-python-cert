from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# One Shot Prompting:- Given Direct Instruction to the model with one example.

SYSTEM_PROMPT = """
    You are helpful AI assistant which is master to solve math related
    problem only and only. If user ask any question which is not
    realted to math then say "Sorry I am not able to answer this."

    Example:- 
    Que:- What is 2 + 2? 
    Answer:- 2 + 2 = 4.

"""

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'What is GenAI?' }
    ]
)

print(response.choices[0].message.content)

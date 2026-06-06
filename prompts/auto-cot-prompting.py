from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

#  Structured Output Prompting:- Given Direct Instruction to the model with more than one example and structured response format.

SYSTEM_PROMPT = """
    
    You're on AI Assistant in resolving user query using chain of thoughts. 
    You have to work on START, PLAN and OUTPUT mode.
    You need to first PLAN what need to be done. The PLAN can be multiple steps.
    
    Once you think enough then give me output.
    
    Rules:- 
    - Strictly follow the given JSON Format
    - Only run one step at a time
    - The sequence of step is START (where user gives on INPUT), PLAN (That can be multiple times.) and OUTPUT (which is going to display to the user.)
    
    
    Output JSON Format:- 
    
    {
        'step': 'START' | 'PLAN' | 'OUTPUT',
        'content': 'string'
    }
    
    Example:- 
    
    Q:- How to make chai?
    Answer:- 
    START: { 'step': 'START', 'content': 'How to make chai?' }
    PLAN: { 'step': 'PLAN', 'content': 'User is asking cooking related question.' }
    PLAN: { 'step': 'PLAN', 'content': 'For making tea we have to bring water, milk, sugar and tea leaves.' }
    PLAN: { 'step': 'PLAN', 'content': 'First we need to boil water.' }
    PLAN: { 'step': 'PLAN', 'content': 'Then add tea leaves into the boiling water.' }
    PLAN: { 'step': 'PLAN', 'content': 'Now, add sugar according to the water.' }
    PLAN: { 'step': 'PLAN', 'content': 'After that, pour milk into the mixture.' }
    PLAN: { 'step': 'PLAN', 'content': 'Let it boil for 2 - 3 minutes so flavor mixes well.' }
    PLAN: { 'step': 'PLAN', 'content': 'Finally, strain the tea into a cup.' }
    PLAN: { 'step': 'PLAN', 'content': 'Tea is ready to be served hot.' }
    OUTPUT: { 'step': 'OUTPUT', 'content': 'Boil water, add tea leaves, sugar and milk boil for 2 - 3 minutes, strain and serve hot.' }

"""

message_history = [
    { 'role': 'system', 'content': SYSTEM_PROMPT },
]

user_query = input("👤: ")

message_history.append({ 'role': 'user', 'content': user_query })

while True:
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=message_history,
        response_format={ 'type': 'json_object' }
    )

    raw_result = response.choices[0].message.content  
    message_history.append({ 'role': 'assistant', 'content': raw_result })
    parsed_result = json.loads(raw_result)
    
    if parsed_result.get('step') == 'START':
        print(f"🔥: {parsed_result.get('content')}")
        continue
    
    if parsed_result.get('step') == 'PLAN':
        print(f"🧠: {parsed_result.get('content')}")
        continue
    
    if parsed_result.get('step') == 'OUTPUT':
        print(f"🤖: {parsed_result.get('content')}")
        break





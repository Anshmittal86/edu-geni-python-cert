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

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'How to make momos?' },
        { 'role': 'assistant', 'content': json.dumps({ 'step': 'START', 'content': 'How to make momos?' }) },
        { 'role': 'assistant', 'content': json.dumps({ 'step': 'PLAN', 'content': 'assistant is asking for a recipe on how to make momos.' }) },
        { 'role': 'assistant', 'content': json.dumps({"step": "PLAN", "content": "To make momos, we need ingredients like flour for the dough, vegetables or meat for the filling, and some spices."}) },
        { 'role': 'assistant', 'content': json.dumps({"step": "PLAN", "content": "First, we need to make the dough by mixing flour with water and kneading it until smooth."}) },
        { 'role': 'assistant', 'content': json.dumps({"step": "PLAN", "content": "Next, let the dough rest for about 20-30 minutes to become more pliable."}) },
        { 'role': 'assistant', 'content': json.dumps({"step": "PLAN", "content": "While the dough is resting, we can prepare the filling by chopping the vegetables or meat and mixing them with spices."}) },
        { 'role': 'assistant', 'content': json.dumps({"step": "PLAN", "content": "Once the filling is ready, we can divide the dough into small portions and roll each portion into a thin circle."}) },
        { 'role': 'assistant', 'content': json.dumps({"step": "PLAN", "content": "Now, place a spoonful of filling in the center of each dough circle and fold the edges together to seal them."}) },
        { 'role': 'assistant', 'content': json.dumps({"step": "PLAN", "content": "After sealing the momos, we can prepare to steam them in a steamer for about 10-15 minutes until cooked."}) },
        { 'role': 'assistant', 'content': json.dumps({"step": "PLAN", "content": "Finally, we can serve the momos with a dipping sauce of our choice."}) },
        { 'role': 'assistant', 'content': json.dumps({"step": "OUTPUT", "content": "To make momos, prepare the dough with flour and water and let it rest for 20-30 minutes. Prepare the filling with chopped vegetables or meat mixed with spices. Roll the dough into thin circles, place the filling inside, seal the edges, and steam the momos for 10-15 minutes. Serve with dipping sauce."}) },
    ]
)


print(response.choices[0].message.content)

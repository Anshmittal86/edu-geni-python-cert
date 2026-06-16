from openai import OpenAI
from dotenv import load_dotenv
import json
import os
import subprocess

load_dotenv()

client = OpenAI()

def read_file(file_path: str) -> str:
    """ Reads the content of the file at the given path."""
    print(f"Tool Called: read_file, {file_path}")
    
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_file(input_json: str) -> str:
    """ write the content of the file."""
    print(f"Tool called: write_file {repr(input_json[:200])}...")
    
    try:
        params = json.loads(input_json)
    except json.JSONDecodeError as e:
        return f"⚔️ JSON Error: {str(e)[:100]}. Input is invalid."
    
    file_path = params.get('file_path', 'File path not found')
    content = params.get('content', 'Content not found')
    
    if file_path or content is None:
        return '⚔️ Missing file_path and content in params'
    
    try:
        with open(file_path, 'w') as f:
            f.write(content)
            return f"✅ File Written Successfully."
        
    except Exception as e:
        return f"⚔️ Write Error: {str(e)}"

def list_directory(dir_path: str = ".") -> str:
    """Lists files and directories in the given path."""
    print(f"Tool called: list_directory, {dir_path}")
    
    try:
        items = os.listdir(dir_path)
        return "\n".join(items)
    except Exception as e:
        return f"Error Listing Directory: {str(e)}"

def run_shell(input_json: str) -> str:
    print(f'🔨 Tool Called: run_shell {json.loads(input_json)["cmd"]}')
    
    params = json.loads(input_json)
    cmd = params.get('cmd', 'not found')
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout + result.stderr
    
        return f"Exit code: {result.returncode} \n Output: {output}"
    except subprocess.TimeoutExpired:
        return "Command Timed out"
    
    except Exception as e:
        return f"Error running command: {str(e)}"

#  Structured Output Prompting:- Given Direct Instruction to the model with more than one example and structured response format.

available_tools = {
    'read_file': read_file,
    'write_file': write_file,
    'list_directory': list_directory,
    'run_shell': run_shell
}

SYSTEM_PROMPT = """
    
    You're on AI Assistant in resolving user query using chain of thoughts. 
    You have to work on START, PLAN, ACTION, OBSERVE and OUTPUT mode.
    You need to first PLAN what need to be done. The PLAN can be multiple steps.
    
    Once you think enough then give me output.
    
    Rules:- 
    - Strictly follow the given JSON Format
    - Only run one step at a time
    - The sequence of step is START (where user gives on INPUT), PLAN (That can be multiple times.), ACTION( function calling based on the user query), OBSERVE (understand the tool result) and finally OUTPUT (which is going to display to the user.)
    - Guide the user based on the weather info that what precautions you should have to follow if any situation you are contacting the weather.
    
    
    Output JSON Format:- 
    
    {
        'step': 'START' | 'PLAN' | 'ACTION' | 'OBSERVE' | 'OUTPUT',
        'content': 'string'
    }
    
    Available Tools:
    - read_file(file_path: str): Reads content from a file
    - list_directory(dir_path: str): lists files in directory
    - write_file(input_json: str): {'file_path': 'file.py', 'content': 'code here' }
    - run_shell(input_jsonL str): { 'cmd': 'ls', 'cwd': '.' }
    
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
    
    Q:- What is the weather of mumbai?
    Answer:- 
    START: { 'step': 'START', 'content': 'What is the weather of mumbai?' }
    PLAN: { 'step': 'PLAN', 'content': 'Seems like user is interested in weather report.' }
    PLAN: { 'step': 'PLAN', 'content': 'First I have to see the list of available tools to check the any tool available for solving this query.' }
    PLAN: { 'step': 'PLAN', 'content': 'Yes, we have a tool of get_weather to get the weather info.' }
    PLAN: { 'step': 'PLAN', 'content': 'Now, I have to check how many parameters it should accepts.' }
    PLAN: { 'step': 'PLAN', 'content': 'Ok, the tool of get_weather accept only one parameter which is city name of find the latest weather report.' }
    ACTION: { 'step': 'ACTION', 'tool': 'get_weather', 'input': 'mumbai' }
    OBSERVE: { 'step': 'OBSERVE', 'tool': 'get_weather', 'input': 'mumbai', 'output': '30c' }
    PLAN: { 'step': 'PLAN', 'content': 'ok, The current weather of delhi is 30c.' }
    OUTPUT: { 'step': 'OUTPUT', 'content': 'Mumbai weather is 30 degree celcius. Drink Water on time and maintain hydration level.' }

"""

message_history = [
    { 'role': 'system', 'content': SYSTEM_PROMPT },
]

while True:
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
        
        if parsed_result.get('step') == 'ACTION':
            tool_name = parsed_result.get('tool')
            tool_input = parsed_result.get('input')
            
            print(f'🔨 Tool name: {tool_name}, Input: {tool_input}')
            
            # function_name(function_input)
            if available_tools.get(tool_name, False) != False:
                tool_output = available_tools[tool_name](tool_input)
                
                print(f'🔨 Tool name: {tool_name}, Output: {tool_output}')
                
                message_history.append({ 'role': 'assistant', 'content': json.dumps({ 'step': 'OBSERVE','tool': tool_name, 'input': tool_input, 'output': tool_output }) })
                continue
        
        if parsed_result.get('step') == 'OUTPUT':
            print(f"🤖: {parsed_result.get('content')}")
            break





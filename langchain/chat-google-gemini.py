from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash',
    temperature=0.7,
    timeout=30,
    max_retries=2
)

# messages=[
#     { 'role': 'system', 'content': 'You are expert in song writing?' },
#     { 'role': 'user', 'content': 'Write a happy birthday song for my friend. Friend name is Dhairya.' },
# ]

messages=[
    ( 'system', 'You are expert in song writing?' ),
    ( 'user', 'Write a happy birthday song for my friend. Friend name is Dhairya.' ),
]

response = model.invoke(messages)

print(response.text)
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from concurrent.futures import ThreadPoolExecutor #Multithreading
from itertools import chain
from dotenv import load_dotenv
from openai import OpenAI
import ast
load_dotenv()

client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_existing_collection(
    url='http://localhost:6333',
    collection_name='learning-rag',
    embedding=embedding_model
)

user_query = input("👤: ")

SYSTEM_PROMPT = """
    Your task is to break user query into multiple sub queries.
    
    Rule:- Strictly Follow Maximum Sub Query Length: 3
    
    Example:- 
    Query:- What is FS Module in Node.JS?
    Output: [
        'What is Fs Module?'
        'What is Node.JS?'
        'What is FS Module in Node.JS?'
    ]
"""

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': user_query }
    ]
)

list_in_string = response.choices[0].message.content.strip()
sub_queries = ast.literal_eval(list_in_string)


def retrieve_chunks(query: str):
    return vector_store.similarity_search(query=query)

with ThreadPoolExecutor() as executor:
    all_chunks = executor.map(retrieve_chunks, sub_queries)
    

flattened_chunks = list(chain.from_iterable(all_chunks))

unique_chunks = list({doc.page_content: doc for doc in flattened_chunks}.values())

print(unique_chunks)

SYSTEM_PROMPT_SECOND = f"""
        You are a helpful assistant who answer user's query by using the following pieces of context with the page no. so that user can refer.
        If you don't know the answer, just say that I don't know write the reason why you are not able to give the answer only give the 2 to 3 live max reason instead of just saying I don't know, don't try to make up an answer.
        
        context: {[doc.page_content for doc in unique_chunks]}
"""

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT_SECOND },
        { 'role': 'user', 'content': user_query }
    ]
)

print(response.choices[0].message.content)
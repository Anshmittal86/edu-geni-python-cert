from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model='text-embedding-3-large',
)

vector_store = QdrantVectorStore.from_existing_collection(
    url='http://localhost:6333',
    collection_name='learning-rag',
    embedding=embedding_model
)

while True:
    user_query = input("👤: ")
    
    step_back_prompt = f"""
        You are helpful AI Assistant. Your task is to take the user's original query and convert to the conceptual question.
        
        Example:-
        Query:- Which year Mahatma Gandhi's Born?
        step-back:- What is Mahatma Gandhi personal History?
        
        Query:- Which skills is required to become a software developer?
        step-back:- How to become a software developer?
    """
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            { 'role': 'system', 'content': step_back_prompt },
            { 'role': 'user', 'content': user_query }
        ]
    )
    
    step_back_query = response.choices[0].message.content.strip()
    
    relevant_chunks = vector_store.similarity_search(query=step_back_query)
    
    SYSTEM_PROMPT_SECOND = f"""
        You are a helpful assistant who answer user's query by using the following pieces of context with the page no. so that user can refer.
        If you don't know the answer, just say that I don't know write the reason why you are not able to give the answer only give the 2 to 3 live max reason instead of just saying I don't know, don't try to make up an answer.
        
        context: {relevant_chunks}
    """
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            { 'role': 'system', 'content': SYSTEM_PROMPT_SECOND },
            { 'role': 'user', 'content': user_query }
        ]
    )
    
    pdf_response = response.choices[0].message.content
    
    print(f"🤖: {pdf_response}")
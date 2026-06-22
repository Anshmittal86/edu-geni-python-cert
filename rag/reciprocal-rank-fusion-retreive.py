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
    model='text-embedding-3-large'
)

vector_store = QdrantVectorStore.from_existing_collection(
    url='http://localhost:6333',
    collection_name='learning-rag',
    embedding=embedding_model
)

SYSTEM_PROMPT = """
    You are helpful AI Assistant. 
    Your task is to break user query into multiple sub queries.
    
    Rule:- Strictly Follow Maximum Sub Query Length: 3
    
    Example:-
    Query:- What is FS Module in Node.JS?
    Output: [
        'What is Fs Module?',
        'What is Module?',
        'What is Node.JS?'
    ]
"""

while True:
    user_query = input("👤: ")
    
    response = client.chat.completions.create(
    model='gpt-4o-mini',
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
        all_chunks = list(executor.map(retrieve_chunks, sub_queries))

    rankings = []
    
    def get_doc_id(doc):
        return doc.page_content.strip()[:50]
    
    for result in all_chunks:
        rankings.append([get_doc_id(doc) for doc in result])
    
    # Reciprocal Rank Fusion
    def reciprocal_rank_fusion(rankings, k=60):
        scores = {}
        
        for ranking in rankings:
            for rank, doc_id in enumerate(ranking):
                scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
        
        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        return [doc_id for doc_id, score in sorted_docs]
    
    # Get Final Ranked DocIDs
    final_doc_ids = reciprocal_rank_fusion(rankings)
    
    doc_map = {get_doc_id(doc): doc for doc in chain.from_iterable(all_chunks)}
    
    ranked_chunks = [doc_map[doc_id] for doc_id in final_doc_ids if doc_id in doc_map ]
    
    
    SYSTEM_PROMPT_SECOND = f"""
        You are a helpful assistant who answer user's query by using the following pieces of context with the page no. so that user can refer.
        If you don't know the answer, just say that I don't know write the reason why you are not able to give the answer only give the 2 to 3 live max reason instead of just saying I don't know, don't try to make up an answer.
        
        context: {[doc.page_content for doc in ranked_chunks]}
    """
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
                { 'role': 'system', 'content': SYSTEM_PROMPT_SECOND },
                { 'role': 'user', 'content': user_query }
            ]
        )

    print(response.choices[0].message.content)
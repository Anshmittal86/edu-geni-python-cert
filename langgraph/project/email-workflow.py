import uuid
import os
from IPython.display import Image, display
from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Literal
from langchain_openai import ChatOpenAI
from langgraph.types import Command, interrupt
from dotenv import load_dotenv

load_dotenv()

class EmailClassification(TypedDict):
    intent: Literal['question', 'bug', 'billing', 'feature', 'complex']
    urgency: Literal['Low', 'medium', 'high', 'critical']
    topic: str
    summary: str

class EmailAgentState(TypedDict):
    # Raw email data
    email_content: str
    sender_email: str
    email_id: str
    
    # Classification result
    classification: EmailClassification | None
    
    # Bug Tracking
    ticket_id: str | None
    
    # Raw Search results
    search_results: list[str] | None
    customer_history: dict | None
    
    # Generated content
    draft_response: str | None
    
# Define Nodes
def read_email(state: EmailAgentState) -> EmailAgentState:
    """Extract and parse email content"""
    pass

llm = ChatOpenAI(model='gpt-4o-mini')

def classify_intent(state: EmailAgentState) -> EmailAgentState:
    """Use LLM to classify email intent and urgency the route accordingly"""
    
    # Create structures LLM that returns EmailClassification dict
    structured_llm = llm.with_structured_output(EmailClassification)
    
    classification_prompt = f"""
    Analyze this customer email and classify it:
    
    Email: {state['email_content']}
    From: {state['sender_email']}
    
    Provide classification, including intent, urgency, topic and summary.
    """
    
    classification = structured_llm.invoke(classification_prompt)
    
    # Store classification as a single dict in state

    return {'classification': classification}

def search_documentation(state: EmailAgentState) -> EmailAgentState:
    """Search knowledge base for relevant information"""
    
    # Build search query from classification
    classification = state.get('classification', {})
    query = f"{classification.get('intent', "")} {classification.get('topic', "")}"
    
    try:
        # Implement search logic here
        search_result = [
            "--Search_result_1--",
            "--Search_result_2--",
            "--Search_result_3--",
        ]
    except SystemError as e:
        search_result = [f"Search temporarily unavailable: {str(e)}"]
        
        
    return {'search_results': search_result}

def bug_tracking(state: EmailAgentState) -> EmailAgentState:
    """Create or update bug tracking ticket"""
    
    ticket_id = f"BUG_{uuid.uuid4()}"
    
    return {'ticket_id': ticket_id}

def write_response(state: EmailAgentState) -> Command[Literal['human_review', 'send_reply']]:
    """Generate response using context and route based on quality"""
    
    classification = state.get('classification', {})
    
    # Format context from raw state data on demand
    context_sections = []
    
    if state.get('search_results'):
        # Format search result for the prompt
        formatted_docs = "\n".join([f"-{doc}" for doc in state['search_results']])
        
        context_sections.append(f"Relevant documentation: \n{formatted_docs}")
        
    if state.get('customer_history'):
        # Format customer data for the prompt
        context_sections.append(f"Customer tier: {state['customer_history'].get('tier', 'standard')}")
        
    
    # BUild the prompt with formatted context
    draft_prompt = f"""
    Draft a response to this customer 
    email:
    {state['email_content']}
    
    Email intent: {classification.get('intent', 'unknown')}
    
    Urgency Level: {classification.get('urgency', 'unknown')}
    
    {chr(10).join(context_sections)}
    
    Guidelines:
    - Be professional and helpful
    - Address their specific concern
    - Use the provided documentation when relevant
    - Be brief
    """
    
    response = llm.invoke(draft_prompt)
    
    # Determine if human review is needed based on urgency and intent
    
    needs_review = (
        classification.get('urgency') in ['high', 'critical'] or classification.get('intent') == 'complex'
    )
    
    if needs_review: 
        goto = 'human_review'
        print('Needs Approval')
    else: 
        goto = 'send_reply'
    
    return Command(
        update={"draft_response": response.content},
        goto=goto
    )
    
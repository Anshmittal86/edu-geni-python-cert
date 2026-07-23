import uuid
import os
from IPython.display import Image, display
from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import InMemorySaver
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

def human_review(state: EmailAgentState) -> Command[Literal['send_reply', END]]:
    """Pause for human review using interrupt and route based on decision"""

    classification = state.get('classification', {})
    
    # Interrupt() must come first - any code before it will re-run on resume
    human_decision = interrupt({
        'email_id': state.get('email_id'),
        'original_email': state.get('email_content'),
        'draft_response': state.get('draft_response'),
        'urgency': classification.get('urgency'),
        'intent': classification.get('intent'),
        'action': 'Please review and approve/edit this response'
    })
    
    if human_decision.get('approved'):
        return Command(
            update={
                'draft_response': human_decision.get('edited_response', state.get('draft_response'))
            },
            goto='send_reply'
        )
    else:
        return Command(update={}, goto=END)

def send_reply(state: EmailAgentState) -> EmailAgentState:
    """Send the email response"""
    
    # Integrate with a email service
    print(f"Sending reply: {state['draft_response'][:60]}...")
    return {}
    

# Graph Builder
builder = StateGraph(EmailAgentState)

# Register nodes
builder.add_node('read_email', read_email)
builder.add_node('classify_intent', classify_intent)
builder.add_node('search_documentation', search_documentation)
builder.add_node('bug_tracking', bug_tracking)
builder.add_node('write_response', write_response)
builder.add_node('human_review', human_review)
builder.add_node('send_reply', send_reply)

# Connect Edges
builder.add_edge(START, 'read_email')
builder.add_edge('read_email', 'classify_intent')
builder.add_edge('classify_intent', 'search_documentation')
builder.add_edge('classify_intent', 'bug_tracking')
builder.add_edge('search_documentation', 'write_response')
builder.add_edge('bug_tracking', 'write_response')
builder.add_edge('send_reply', END)

memory = InMemorySaver()
config = { 'configurable': { 'thread_id': '1' } }
graph = builder.compile(checkpointer=memory)

# print(graph.get_graph().draw_mermaid())

# Test with urgent billing issue
initial_state = {
    'email_content': 'I was charged twice for my subscription! This is urgent!',
    'sender_email': 'customer@gmail.com',
    'email_id': 'email_123'
}

# Run with a thread_id for persistence
config = { 'configurable': {'thread_id': 'customer_123'} }
result = graph.invoke(initial_state, config)

# The graph will pause at human_review
print(f'Draft ready for review: {result['draft_response'][:60]}...\n')

# Provide human input to resume
human_response = Command(
    resume={
        'approved': True
    }
)

# Resume execution
final_result = graph.invoke(human_response, config)
print('Email sent successfully')
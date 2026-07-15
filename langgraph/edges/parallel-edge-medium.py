from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph
from langgraph.types import Command
from typing import Annotated, TypedDict, List, Literal
import operator

load_dotenv()

class State(TypedDict):
    nlist: Annotated[List[str], operator.add]
    

def node_a(state: State):
    print(f'node a is receiving {state["nlist"]}')
    note = 'A'
    return(State(nlist=[note]))

def node_b(state: State):
    print(f'node b is receiving {state["nlist"]}')
    note = 'B'
    return(State(nlist=[note]))

def node_bb(state: State):
    print(f'node bb is receiving {state["nlist"]}')
    note = 'BB'
    return(State(nlist=[note]))

def node_c(state: State):
    print(f'node c is receiving {state["nlist"]}')
    note = 'C'
    return(State(nlist=[note]))

def node_cc(state: State):
    print(f'node cc is receiving {state["nlist"]}')
    note = 'CC'
    return(State(nlist=[note]))

def node_d(state: State):
    print(f'node d is receiving {state["nlist"]}')
    note = 'D'
    return(State(nlist=[note]))


# Graph Builder 
builder = StateGraph(State)

# Define a Nodes
builder.add_node('node_a', node_a)
builder.add_node('node_b', node_b)
builder.add_node('node_bb', node_bb)
builder.add_node('node_c', node_c)
builder.add_node('node_cc', node_cc)
builder.add_node('node_d', node_d)

# Define a Edges
builder.add_edge(START, 'node_a')

builder.add_edge('node_a', 'node_b')
builder.add_edge('node_a', 'node_c')

builder.add_edge('node_b', 'node_bb')
builder.add_edge('node_c', 'node_cc')

builder.add_edge('node_bb', 'node_d')
builder.add_edge('node_cc', 'node_d')

builder.add_edge('node_d', END)

# Compile a graph
graph = builder.compile()

# print(graph.get_graph().draw_mermaid())

initial_state = State(
    nlist=['Hey How are you']
)

updated_state = graph.invoke(initial_state)
print(updated_state)

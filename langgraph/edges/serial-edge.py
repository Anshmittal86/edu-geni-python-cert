from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict, List

load_dotenv()

class State(TypedDict):
    nlist: List[str]
    
    
def node_a(state: State):
    print(f'node a is receiving {state["nlist"]}')
    
    note = 'Hello World from Node a'
    
    return(State(nlist=[note]))

# Graph Builder
graph_builder = StateGraph(State)

# Define a node
graph_builder.add_node('node_a', node_a)

# Define a Edge
graph_builder.add_edge(START, 'node_a')
graph_builder.add_edge('node_a', END)

graph = graph_builder.compile()

# print(graph.get_graph().draw_mermaid())

initial_state = State(
    nlist= ['Hello Node a, How are you']
)

updated_state = graph.invoke(initial_state)
print(updated_state)
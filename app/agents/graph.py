from langgraph.graph import MessagesState, StateGraph, START, END
from typing import TypedDict
from agents.model import bound_model
from agents.model import tool_node


class GraphState(MessagesState):
    user_name: str
    
def should_continue(state: MessagesState):
    """Return the next node to execute."""
    last_message = state["messages"][-1]
    # If there is no function call, then we finish
    if not last_message.tool_calls:
        return END
    # Otherwise if there is, we continue
    return "action"


# Define the function that calls the model
async def call_model(state: MessagesState):
    response = await bound_model.ainvoke(state["messages"])
    return {"messages": response}

# Define a new graph
workflow = StateGraph(GraphState)

# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("action", tool_node)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    ["action", END],
)
workflow.add_edge("action", "agent")

graph = workflow.compile()
from langgraph.graph import MessagesState, StateGraph, START
from langgraph.prebuilt import tools_condition, ToolNode
from agents.model import bound_model
from agents.model import tools


class GraphState(MessagesState):
    user_name: str
    
# Define the function that calls the model
async def call_model(state: MessagesState):
    response = await bound_model.ainvoke(state["messages"])
    return {"messages": response}

# Define a new graph
workflow = StateGraph(GraphState)

# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode(tools))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

graph = workflow.compile()
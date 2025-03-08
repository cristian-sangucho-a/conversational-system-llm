from langgraph.graph import MessagesState, StateGraph, START
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import tools_condition, ToolNode
from agents.model import bound_model
from agents.model import tools
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

memory = MemorySaver()

class GraphState(MessagesState):
    user_name: str

# Define the function that calls the model


async def call_model(state: GraphState):
    system_message = SystemMessage(
        content=f"Hello i'm {state['user_name']}, you're mi personal asistant")
    response = await bound_model.ainvoke([system_message] + state['messages'])
    return {"messages": response}

# Define a new graph
workflow = StateGraph(GraphState)

# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode(tools))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

graph = workflow.compile(checkpointer=memory)

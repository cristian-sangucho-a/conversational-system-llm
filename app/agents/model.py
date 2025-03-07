import os
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

from dotenv import load_dotenv

load_dotenv()  

api_key = os.getenv("MISTRAL_API_KEY")
print(api_key)  

model = ChatMistralAI(
    model='mistral-medium',
    temperature=0,
    api_key=api_key
)

@tool
def search(query: str):
    """Call to surf the web."""
    return "It's sunny in San Francisco."


tools = [search]
tool_node = ToolNode(tools)
bound_model = model.bind_tools(tools)
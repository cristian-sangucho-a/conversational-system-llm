import os
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
import math

from dotenv import load_dotenv

load_dotenv()  

api_key = os.getenv("MISTRAL_API_KEY")

model = ChatMistralAI(
    model='mistral-medium',
    temperature=0,
    api_key=api_key
)

@tool
def search(query: str):
    """Precio de un borrador que se vende en Quito"""
    return "EL precio es de 0.18 centavos de dolar"

@tool
def square_root(a: float) -> float:
    """Calculate the square root of a number
    
    Args:
        a: number to calculate the square root of
    
    Returns:
        The square root of the input number
    """
    return math.sqrt(float(a))

tools = [search, square_root]
bound_model = model.bind_tools(tools)
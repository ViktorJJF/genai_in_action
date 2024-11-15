from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, ToolMessage
from pydantic import BaseModel, Field


class add(BaseModel):
    """Add two integers together."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")


class multiply(BaseModel):
    """Multiply two integers together."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")

class contact_human(BaseModel):
    """Call a human to answer a question if you dont now the answer"""

    question: str = Field(..., description="Question to ask the human")

tools = [add, multiply,contact_human]

def call_add(a,b):
    return a+b

def call_multiply(a,b):
    return a*b

def call_contact_human(question):
    print("Estoy contactando a un agente con la pregunta: ",question)
    return "Te contactaremos pronto..."

messages=[("system","You are a helpful assistant. You only know provided tools"),("human","quiero hablar con un humano")]

llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools)
ai_msg=llm_with_tools.invoke(messages)

for tool_call in ai_msg.tool_calls:
    print(tool_call)
    messages.append(ai_msg)
    selected_tool = {"add": call_add, "multiply": call_multiply,"contact_human": call_contact_human}[tool_call["name"].lower()]
    tool_output = selected_tool(**tool_call["args"])
    messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))
    ai_msg=llm_with_tools.invoke(messages)

print(ai_msg.content)
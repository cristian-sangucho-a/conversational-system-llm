from sqlalchemy.ext.asyncio import AsyncSession
from repositories.message_repository import MessageRepository
from langchain_core.messages import HumanMessage, AIMessage
from agents.graph import graph 

class ChatService:
    def __init__(self, db: AsyncSession):
        self.message_repository = MessageRepository(db)
        
    async def chat(self, message: str, user_id: int, conversation_id: int):
        
        # get the conversation messages
        messages_of_conversation = await self.message_repository.get_messages_by_conversation(conversation_id)
        
        # type input messages
        chat_history = []
        for msg in messages_of_conversation:
            if msg["role"] == "user":
                chat_history.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "ai":
                chat_history.append(AIMessage(content=msg["content"]))
        
        chat_history.append(HumanMessage(content=msg["message"]))
        
        response = await graph.ainvoke({
            "user_name": str(user_id),
            "messages": chat_history
        })
        ai_response = response["messages"][-1].content
        
        await self.message_repository.save_request_message(
            text=ai_response,
            role="ai",
            conversation_id=conversation_id
        )
        
        return ai_response  
        

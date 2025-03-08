from sqlalchemy.ext.asyncio import AsyncSession
from repositories.message_repository import MessageRepository
from repositories.user_repository import UserRepository
from langchain_core.messages import HumanMessage, AIMessage
from agents.graph import graph


class ChatService:
    def __init__(self, db: AsyncSession):
        self.message_repository = MessageRepository(db)
        self.user_repository = UserRepository(db)

    async def chat(self, message: str, user_id: int, conversation_id: int):

        # get the conversation messages
        messages_of_conversation = await self.message_repository.get_messages_by_conversation(conversation_id)

        # get username
        username = await self.user_repository.get_username(user_id)

        # type input messages
        chat_history = []
        for msg in messages_of_conversation:
            if msg.role == "user":
                chat_history.append(HumanMessage(content=msg.text))
            elif msg.role == "ai":
                chat_history.append(AIMessage(content=msg.text))
        # add new message
        chat_history.append(HumanMessage(content=message))

        # config
        config = {"configurable": {"thread_id": str(conversation_id)}}

        # call the graph
        response = await graph.ainvoke(
            {
                "messages": chat_history,
                "user_name": username
            },
            config
        )
        ai_response = response["messages"][-1].content

        # save the response
        await self.message_repository.save_request_message(
            text=ai_response,
            role="ai",
            conversation_id=conversation_id
        )

        return ai_response

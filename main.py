from langchain.schema import HumanMessage, SystemMessage
from langchain_intro.chatbot import chat_model


if __name__ == '__main__':
    message = [
        SystemMessage(
            content="""You're an assistant knowledgeable about healthcare. Only answer healthcare-related questions."""
        ),
        HumanMessage(
            content="""What is Medicaid managed care?"""
        )
    ]

    print(chat_model.invoke(message))

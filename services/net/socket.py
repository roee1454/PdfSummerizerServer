import asyncio
import websockets
from os import system
from datetime import datetime
from dotenv import load_dotenv
from dataclasses import dataclass
from ..model import generate_response

load_dotenv()


@dataclass
class Message():
    chatId: str
    createdAt: datetime
    content: str
    type: str
    hasFile: bool


    def to_object(self) -> dict:
        return {
            "chatId": self.chatId,
            "createdAt": self.createdAt,
            "content": self.content,
            "type": self.type,
            "hasFile": self.hasFile
        }



async def handle_client(websocket):
    conversation_history = ""
    try:
        async for message in websocket:
            conversation_history += f"User: {message}\nAssistant:"
            print(conversation_history)
            print("Generating response...")
            response = await generate_response(conversation_history.strip())
            print(response)
            conversation_history += f" {response}\n"
            # Todo: Return a type of message
            response_to_return = Message()

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client disconnected: {e}")


async def init_socket():
    async with websockets.serve(handle_client, "localhost", 5000):
        system("clear")
        print("WebSocket server started on ws://localhost:5000")
        await asyncio.Future()
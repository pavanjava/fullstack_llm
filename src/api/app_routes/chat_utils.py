from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from src.core.knowledge_agent import KnowledgeAgent
from src.core.text2sql import Text2SqlAgent

knowledge_destination = "/Users/pavanmantha/Pavans/PracticeExamples/DataScience_Practice/LLMs/llama_index_tutorials/fullstack_llm/data"
chat_routes = r = APIRouter()


class Payload(BaseModel):
    query: str


@r.post('/chat')
async def chat(request: Payload):
    try:
        knowledge_agent = KnowledgeAgent(path=knowledge_destination)
        sql_agent = Text2SqlAgent()

        if 'database' in request.query:
            return {'data': sql_agent.query(prompt=request.query)}
        else:
            return {'data': knowledge_agent.query(user_query=request.query)}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

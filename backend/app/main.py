from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

app = FastAPI(
    title="智能法律顾问API",
    description="基于大语言模型的虚拟法律顾问后端服务",
    version="0.1.0"
)

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    references: Optional[List[str]] = None

@app.get("/")
async def root():
    return {"message": "智能法律顾问API服务运行中", "status": "active"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    与法律顾问对话的接口
    """
    # TODO: 集成LLM模型和对话逻辑
    return ChatResponse(
        response="这是一个临时回复。法律大脑正在开发中...",
        conversation_id=request.conversation_id or "default_conv",
        references=None
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="0.0.0.0", port=8000)
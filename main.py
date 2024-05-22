from fastapi import FastAPI
from typing import Union
from utils import llm_processor
from model.llm_chat import LLMChatRequest
from huggingface_hub import login
import uvicorn
import os

app = FastAPI()


def pre_config():
    login(os.getenv("HF_TOKEN"))


@app.on_event("startup")
async def startup_event():
    pre_config()
    print("FastAPI application is starting...")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/v0/llmchat")
async def llmchat(llm_chat_request: LLMChatRequest) -> dict:
    chat_model = llm_chat_request.llm_model
    chat_query = llm_chat_request.query
    return llm_processor.llm_common_processor(chat_model, chat_query)


# Run the FastAPI server using uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
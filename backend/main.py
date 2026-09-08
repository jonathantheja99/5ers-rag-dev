"""FastAPI server exposing the RAG agent to the React frontend."""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

try:  # supports both `uvicorn main:app` (from backend/) and `uvicorn backend.main:app`
    from agent import RAGAgent
except ImportError:  # pragma: no cover
    from backend.agent import RAGAgent

# Comma-separated list, e.g. "http://localhost:5173,https://support.example.com".
ALLOWED_ORIGINS = [
    o.strip()
    for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")
    if o.strip()
]

agent: RAGAgent | None = None
init_error: str | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Built once at startup so the first user request isn't paying for indexing.
    global agent, init_error
    try:
        agent = RAGAgent()
        print(f"Agent initialized (status={agent.status}, chunks={agent.indexed_chunks}).")
    except Exception as e:
        init_error = f"{type(e).__name__}: {e}"
        print(f"Error initializing agent: {init_error}")
        agent = None
    yield


app = FastAPI(title="The5ers RAG Support Bot", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)


class ChatResponse(BaseModel):
    answer: str


@app.get("/health")
def health():
    if agent is None:
        return {"status": "error", "detail": init_error or "agent not initialized"}
    return {
        "status": agent.status,
        "ready": agent.is_ready(),
        "indexed_chunks": agent.indexed_chunks,
    }


# Declared sync on purpose: get_answer() makes blocking network calls, so FastAPI
# runs this in its threadpool instead of stalling the event loop for every request.
@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    if agent is None:
        raise HTTPException(
            status_code=503,
            detail=f"Agent is not initialized. {init_error or 'Check API keys and logs.'}",
        )

    message = req.message.strip()
    if not message:
        raise HTTPException(status_code=422, detail="Message cannot be empty.")

    try:
        return ChatResponse(answer=agent.get_answer(message))
    except Exception as e:
        print(f"/chat failed: {type(e).__name__}: {e}")
        raise HTTPException(status_code=502, detail=f"Upstream model error: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))

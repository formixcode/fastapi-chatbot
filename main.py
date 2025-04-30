import os
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, Request, Response, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import logging
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Configure OpenAI client
openai.api_key = OPENAI_API_KEY

# Define API key security scheme
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# Define request and response models
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    max_tokens: Optional[int] = 1000
    temperature: Optional[float] = 0.7

class ChatResponse(BaseModel):
    response: str
    
# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Chatbot",
    description="A secure chatbot API built with FastAPI and OpenAI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API key validation dependency
async def verify_api_key(api_key: str = Depends(api_key_header)):
    # For internal use, no API key needed
    if api_key is None:
        return
    
    # For external use, validate API key (implement your own validation logic)
    if api_key != "your-secure-api-key":  # Replace with a secure API key for external access
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )

# Serve React app static files
@app.get("/", response_class=HTMLResponse)
async def serve_react_app():
    return FileResponse("./react/dist/index.html")

# Chat endpoint
@app.post("/api/chat", response_model=ChatResponse, dependencies=[Depends(verify_api_key)])
async def chat(request: ChatRequest):
    try:
        # Convert Pydantic models to dictionaries for OpenAI API
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        # Call OpenAI API with GPT-4o-mini model
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
        )
        
        # Extract and return the response
        return ChatResponse(response=response.choices[0].message.content)
    
    except Exception as e:
        logger.error(f"Error calling OpenAI API: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing chat request: {str(e)}",
        )

# Mount static files after defining routes
app.mount("/assets", StaticFiles(directory="./react/dist/assets"), name="assets")

# Add a route for the Vite icon
@app.get("/vite.svg", response_class=FileResponse)
async def serve_vite_icon():
    return FileResponse("./react/dist/vite.svg")

# Serve other static files from the React build
@app.get("/{path:path}", response_class=HTMLResponse)
async def serve_react_paths(path: str):
    # For any other path, serve the React app's index.html
    return FileResponse("./react/dist/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
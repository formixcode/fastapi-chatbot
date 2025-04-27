from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Chatbot",
    description="A simple chatbot API built with FastAPI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
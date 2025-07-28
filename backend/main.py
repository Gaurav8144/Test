from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production mein yeh specific domain hona chahiye
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/respond")
async def respond(msg: Message):
    if msg.text.lower().strip() == "hello":
        return {"reply": "Hi, how are you?"}
    else:
        return {"reply": "I can only respond to 'hello'."}

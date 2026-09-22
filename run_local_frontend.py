import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import root_agent

app = FastAPI()
session_service = InMemorySessionService()
runner = Runner(agent=root_agent, session_service=session_service, app_name="local_app")
contexts = {}

@app.post("/chat")
async def chat(req: Request):
    body = await req.json()
    message_text = body.get("message", "")
    user_id = body.get("user_id") or "web-user"
    
    session_id = contexts.get(user_id)
    session = None
    if session_id:
        session = session_service.get_session_sync(app_name="local_app", user_id=user_id, session_id=session_id)
    if not session:
        session = session_service.create_session_sync(user_id=user_id, app_name="local_app")
        contexts[user_id] = session.id
        
    message = types.Content(role="user", parts=[types.Part.from_text(text=message_text)])
    events = list(runner.run(new_message=message, user_id=user_id, session_id=session.id))
    
    text_reply = ""
    for event in events:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    text_reply += part.text
                    
    return JSONResponse({"parts": [{"kind": "text", "text": text_reply or "(no response)"}]})

app.mount("/", StaticFiles(directory="frontend/static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)

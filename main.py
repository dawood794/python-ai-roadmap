import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq

# 1. Start the Engine
print("📁 Nexus Secure Database Schema initialized successfully.")

app = FastAPI(title="Nexus AI Engine")

# 2. Add your new Groq Key here
GROQ_API_KEY = "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"
ai_client = Groq(api_key=GROQ_API_KEY)

# 3. Request Schema
class UserQuery(BaseModel):
    prompt: str

# 4. The Home Route
@app.get("/")
def home():
    return {
        "status": "Nexus Secure Database Schema initialized successfully",
        "api_engine": "connected",
        "docs_url": "/docs"
    }

# 5. The AI Chat Route
@app.post("/api/generate-roadmap")
async def generate_roadmap(data: UserQuery):
    if not data.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    try:
        chat_completion = ai_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an expert AI and Machine Learning engineer. Provide a structured roadmap."},
                {"role": "user", "content": data.prompt}
            ],
            model="llama-3.1-8b-instant",
        )
        return {"roadmap": chat_completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
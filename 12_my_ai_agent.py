import os
from openai import OpenAI

print("--- 🤖 INITIALIZING YOUR CUSTOM AI AGENT ---")

# 1. CONNECT TO A FREE HIGH-SPEED AI CLOUD PROVIDER
# We use Groq's ultra-fast cloud server to run an open-source model for free
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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" # We will replace this with a real key next!
)

# 2. DEFINE THE AI'S PERSONALITY (System Prompt)
# This dictates exactly how your AI acts, talks, and thinks!
system_instruction = {
    "role": "system",
    "content": "You are a helpful, brilliant, and witty AI assistant. Keep responses clear and engaging."
}

# 3. INITIALIZE THE MEMORY BANK
conversation_history = [system_instruction]

print("AI Engine Online! Type 'exit' to quit.\n")

while True:
    user_input = input("You 🧑: ")
    if user_input.lower() == 'exit':
        print("Shutting down AI Engine. See ya!")
        break
        
    if not user_input.strip():
        continue

    # Add what the user said to the history
    conversation_history.append({"role": "user", "content": user_input})
    
    print("\nAI is thinking... 🧠")
    
    try:
        # Send the whole conversation history to the cloud brain
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=conversation_history,
            stream=True
        )
        
        print("Custom AI 🤖: ", end="", flush=True)
        ai_response = ""
        
        # Stream the response word-by-word just like a real AI product!
        for chunk in completion:
            if chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                print(text, end="", flush=True)
                ai_response += text
        print("\n" + "_"*50 + "\n")
        
        # Add the AI's response to memory so it remembers the context
        conversation_history.append({"role": "assistant", "content": ai_response})
        
    except Exception as e:
        print(f"\n❌ Connection Error: {e}")
        print("Don't worry! We just need to plug in a valid API key to activate the cloud stream.")
        break
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import openai
import asyncio
import json
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY", "your-openai-key")  # Set environment variable

# Mock integrations
def check_lead_status(lead_id):
    # Mock SQL check
    return {"status": "active"}

def trigger_whatsapp(message, phone):
    # Mock API call
    print(f"Triggered WhatsApp: {message} to {phone}")

def log_to_crm(call_data):
    # Mock logging
    print(f"Logged to CRM: {call_data}")

app = FastAPI()

# Mount static directories for simple bots
app.mount("/lead_qualifier", StaticFiles(directory="lead_qualifier"), name="lead_qualifier")
app.mount("/personal_loan", StaticFiles(directory="personal_loan"), name="personal_loan")

# System prompts
lead_qualifier_prompt = """
You are a Lead Qualifier Voice Bot for a home renovation company. Your task is to ask three yes/no questions to qualify leads:

1. Do you own your home?
2. Is your budget over $10,000?
3. Are you looking to start within 3 months?

If the user answers 'Yes' to all three, classify them as a 'Hot Lead' and offer to transfer the call to a human agent.
If they answer 'No' to any question, politely thank them and end the call.

Speak in a friendly, professional manner. Keep responses concise.
"""

personal_loan_prompt = """
You are a Personal Loan Eligibility Voice Bot for QuickRupee. Your task is to screen callers based on three eligibility checks:

1. Are you a salaried employee?
2. Is your monthly 'in-hand' salary above ₹25,000?
3. Do you reside in a metro city (e.g., Delhi, Mumbai, or Bangalore)?

If the user answers 'Yes' to all three, mark them as 'Eligible' and say an agent will call back within 10 minutes.
If they answer 'No' to any question, gently inform them they do not meet current criteria and end the call.

Speak in a friendly, professional manner. Keep responses concise.
"""

@app.websocket("/ws/{bot_type}")
async def websocket_endpoint(websocket: WebSocket, bot_type: str):
    await websocket.accept()
    conversation = []
    if bot_type == "lead_qualifier":
        system_prompt = lead_qualifier_prompt
    elif bot_type == "personal_loan":
        system_prompt = personal_loan_prompt
    else:
        await websocket.send_text("Invalid bot type")
        await websocket.close()
        return

    # Initial greeting
    initial_message = "Welcome to the bot."
    await websocket.send_text(initial_message)
    conversation.append({"role": "assistant", "content": initial_message})

    while True:
        data = await websocket.receive_text()
        conversation.append({"role": "user", "content": data})
        # Call LLM
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": system_prompt}] + conversation,
            max_tokens=150,
            temperature=0.7
        )
        bot_response = response.choices[0].message.content.strip()
        conversation.append({"role": "assistant", "content": bot_response})
        await websocket.send_text(bot_response)

        # Mock integrations based on response
        if "hot lead" in bot_response.lower():
            check_lead_status("mock_id")
            trigger_whatsapp("You are a hot lead!", "mock_phone")
            log_to_crm({"call": "lead_qualifier", "outcome": "hot_lead"})
        elif "eligible" in bot_response.lower():
            check_lead_status("mock_id")
            trigger_whatsapp("You are eligible!", "mock_phone")
            log_to_crm({"call": "personal_loan", "outcome": "eligible"})
        elif "goodbye" in bot_response.lower():
            log_to_crm({"call": bot_type, "outcome": "ended"})
            break

@app.get("/")
async def get():
    return HTMLResponse("<h1>Voice AI Super-Agent</h1><p>Use WebSocket at /ws/{bot_type} where bot_type is 'lead_qualifier' or 'personal_loan'</p>")
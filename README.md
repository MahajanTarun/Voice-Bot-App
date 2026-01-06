# Voice AI Super Agent (POC as assignment)

This is a **Voice AI “Super-Agent” prototype built for Rural India**.
It talks to people over voice (Hinglish), qualifies home renovation leads, checks loan eligibility, and handles real-time conversations—just like a human agent on a phone call.

The goal: **natural conversations at scale**, capable of handling thousands of calls a day.

* **Voice Bots (Browser based)**
  Talk directly using your mic—no setup, no apps.
* **AI-Powered Super Agent**
  Uses OpenAI to understand context and reply naturally.
* **Standalone Scripts**
  Run simple voice bots locally using your mic and speakers.

You can run everything together or try individual pieces.

---

## Quick Start

### Setup

* Python 3 installed
* An OpenAI API key

```bash
cd super_agent
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
uvicorn main:app --reload
```
App Server: **[http://localhost:8000](http://localhost:8000)**

## Try the Bots
* **Lead Qualifier:**
  [http://localhost:8000/lead_qualifier/](http://localhost:8000/lead_qualifier/)
  Speak “yes / no” to qualify a home-repair lead.

* **Personal Loan Bot:**
  [http://localhost:8000/personal_loan/](http://localhost:8000/personal_loan/)
  Voice-based loan eligibility check.

* **AI Tester (Text):**
  [http://localhost:8000/client.html](http://localhost:8000/client.html)
  Chat with the intelligent agent via WebSocket.

## Docker (Optional)

```bash
docker build -t super-agent .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key super-agent
```

## Tech Stack
* **Backend:** FastAPI + WebSockets
* **AI:** OpenAI GPT
* **Voice (Web):** Web Speech API
* **Voice (Local):** speech_recognition, pyttsx3

## Note
This is a **prototype**, meant for demos and experimentation.
Integration with platforms like **Retell / Twilio** is pending due to time constraints.

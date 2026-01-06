# Voice AI Super-Agent

This is a prototype Voice AI "Super-Agent" for Rural India, built with FastAPI and WebSocket for real-time conversation control between telephony providers and LLMs.

## Features
- WebSocket server for handling real-time voice conversations.
- Integration with OpenAI GPT for intelligent responses.
- Mock integrations for SQL lead checks, WhatsApp messaging, and CRM logging.
- Optimized for low latency with async programming.

## Setup

### Local Development
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key:
   ```
   export OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Run the server:
   ```
   uvicorn main:app --reload
   ```
   The server will start on http://localhost:8000.

### Docker
1. Build the image:
   ```
   docker build -t super-agent .
   ```
2. Run the container:
   ```
   docker run -p 8000:8000 -e OPENAI_API_KEY=your_openai_api_key_here super-agent
   ```

## Usage
- WebSocket endpoints:
  - `/ws/lead_qualifier` for Lead Qualifier bot.
  - `/ws/personal_loan` for Personal Loan Eligibility bot.
- Connect a WebSocket client (e.g., websocat) and send text messages to simulate conversation.
- Example: `websocat ws://localhost:8000/ws/lead_qualifier`

## Testing
Use the included `client.html` for a simple web-based tester. Open it in a browser, select bot type, connect, and send messages to see LLM-driven responses.

## Production
For production, integrate with Retell AI or similar telephony providers. Deploy to AWS/GCP using the Dockerfile.
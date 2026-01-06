# Voice AI Super-Agent Prototype

Hey there! Welcome to this cool prototype of a Voice AI "Super-Agent" built for Rural India. Imagine a smart bot that can chat with people over the phone, qualify leads for home renovations, check loan eligibility, and even negotiate deals—all in real-time using cutting-edge AI. This project is designed to handle thousands of calls daily, speaking fluent Hinglish, and making conversations feel super natural.

## What's Inside This Project?

We've got a bunch of fun stuff here:

- **Simple Voice Bots:** Easy web pages where you can talk to bots for lead qualification and loan checks. They use your browser's built-in voice features—no extra setup needed!
- **Advanced AI Bot:** A powerful server that uses smart AI (from OpenAI) to have intelligent conversations. It can adapt and respond naturally.
- **Standalone Scripts:** If you prefer, run the simple bots directly on your computer using your mic and speakers.

Everything is tied together in one neat package, but you can pick and choose what to try.

## How to Get Started and Run the Whole Thing
w
The heart of this project is the FastAPI server in the `super_agent` folder. It serves up all the bots and handles the AI magic. Let's get it running!

### Step 1: Set Up Your Environment
- Make sure you have Python 3 installed on your computer.
- You'll need an OpenAI API key. If you don't have one, sign up at [OpenAI](https://openai.com) and get your key.

### Step 2: Install and Run
1. Open your terminal and go to the `super_agent` folder: `cd super_agent`
2. Install the needed packages: `pip install -r requirements.txt`
3. Set your OpenAI key: `export OPENAI_API_KEY=your_actual_key_here` (replace with your real key)
4. Start the server: `uvicorn main:app --reload`

Boom! The server is now running on http://localhost:8000. Keep this terminal open.

### Step 3: Explore the Bots
Now that the server is up, open your web browser and try these:

- **Lead Qualifier Bot:** Go to http://localhost:8000/lead_qualifier/. Click "Start Bot," allow microphone access, and answer the questions by speaking "yes" or "no." It's like qualifying a potential customer for home repairs!
- **Personal Loan Bot:** Visit http://localhost:8000/personal_loan/. Same deal—talk to it about loan eligibility.
- **Advanced AI Tester:** Head to http://localhost:8000/client.html. Pick a bot type, connect, and type messages to see how the AI responds intelligently. It's like chatting with a super-smart assistant!

For developers, you can connect WebSocket clients (like tools or code) to `ws://localhost:8000/ws/lead_qualifier` or `ws://localhost:8000/ws/personal_loan` to send and receive messages programmatically.

## Running with Docker (If You Prefer)

If Docker is your thing:

1. In the `super_agent` folder, build the image: `docker build -t super-agent .`
2. Run it: `docker run -p 8000:8000 -e OPENAI_API_KEY=your_key super-agent`

Same as above, but containerized!

## Running the Bots Separately (Optional)

Want to try the simple bots without the full server? No problem!

- For the Lead Qualifier: In a new terminal, run `python3 lead_qualifier/main.py`
- For the Personal Loan: Run `python3 personal_loan/main.py`

These will use your computer's microphone and speakers directly. Speak clearly, and they'll respond!

## What Makes This Special?

- **Real-Time and Fast:** Uses async programming to keep responses snappy (under 800ms latency).
- **AI-Powered:** The advanced bot uses OpenAI's GPT to understand and respond like a human.
- **Integrated:** Mocks connections to databases, WhatsApp, and CRM systems for a full experience.
- **Scalable:** Built to handle many calls, just like a real service.

## Tech Stuff (For the Curious)

- **Backend:** Python with FastAPI for the server, WebSockets for live chats.
- **AI:** OpenAI's API for smart responses.
- **Voice in Browser:** Web Speech API for easy voice interaction.
- **Voice on Desktop:** Libraries like pyttsx3 and speech_recognition for mic/speaker.

## Important Notes

- This is a prototype, so it's for testing and fun. For real-world use, hook it up to phone systems like Retell AI.
- Keep your OpenAI key safe—don't share it!
- If you run into issues, check that your mic is working and you've got the right Python version.

Have fun exploring the future of voice AI! If you have questions or ideas, feel free to tinker. 🚀
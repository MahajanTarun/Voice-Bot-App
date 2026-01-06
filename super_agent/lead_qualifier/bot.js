const synth = window.speechSynthesis;
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.continuous = false;
recognition.lang = 'en-US';

function speak(text) {
    const utter = new SpeechSynthesisUtterance(text);
    synth.speak(utter);
}

function askQuestion(question, callback) {
    speak(question);
    recognition.start();
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript.toLowerCase();
        console.log('Transcript:', transcript);
        if (transcript.includes('yes')) {
            callback(true);
        } else if (transcript.includes('no')) {
            callback(false);
        } else {
            speak("Please say yes or no.");
            askQuestion(question, callback);
        }
    };
    recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
        speak("Sorry, I didn't catch that. Please try again.");
        askQuestion(question, callback);
    };
}

document.getElementById('startBtn').addEventListener('click', () => {
    speak("Welcome to the Lead Qualifier Bot for home renovation services.");
    askQuestion("Do you own your home?", (ans1) => {
        if (!ans1) {
            speak("Thank you for calling. We appreciate your interest. Goodbye.");
            return;
        }
        askQuestion("Is your budget over $10,000?", (ans2) => {
            if (!ans2) {
                speak("Thank you for calling. We appreciate your interest. Goodbye.");
                return;
            }
            askQuestion("Are you looking to start within 3 months?", (ans3) => {
                if (!ans3) {
                    speak("Thank you for calling. We appreciate your interest. Goodbye.");
                    return;
                }
                speak("You are classified as a hot lead. I will transfer you to a human agent now. Thank you.");
            });
        });
    });
});
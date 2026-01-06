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
    speak("Welcome to QuickRupee Personal Loan Eligibility Bot.");
    askQuestion("Are you a salaried employee?", (ans1) => {
        if (!ans1) {
            speak("Thank you for your interest. Unfortunately, you do not meet our current eligibility criteria. Goodbye.");
            return;
        }
        askQuestion("Is your monthly in-hand salary above 25,000 rupees?", (ans2) => {
            if (!ans2) {
                speak("Thank you for your interest. Unfortunately, you do not meet our current eligibility criteria. Goodbye.");
                return;
            }
            askQuestion("Do you reside in a metro city such as Delhi, Mumbai, or Bangalore?", (ans3) => {
                if (!ans3) {
                    speak("Thank you for your interest. Unfortunately, you do not meet our current eligibility criteria. Goodbye.");
                    return;
                }
                speak("Congratulations, you are eligible for a personal loan. An agent will call you back within 10 minutes. Thank you.");
            });
        });
    });
});
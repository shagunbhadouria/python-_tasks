import speech_recognition as sr  # For recognizing speech
import pyttsx3  # For converting text to speech
import datetime  # For getting the current time and date

# Initialize the recognizer and pyttsx3 engine
recognizer = sr.Recognizer()  # Recognizer to listen to user's speech
engine = pyttsx3.init()  # Engine to convert text to speech

def speak(text):
    """Function to speak out the text."""
    engine.say(text)  # Convert text to speech
    engine.runAndWait()  # Wait for the speech to finish

def listen_for_commands():
    """Function to listen for voice commands."""
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Listening...")  # Let the user know it's listening
        audio = recognizer.listen(source)  # Listen for the user's input
        try:
            # Try to recognize speech and convert it to text
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")  # Print what was heard
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")  # If it couldn't understand
            return ""
        except sr.RequestError:
            print("There was an error with the speech service.")  # If there was an issue with the speech recognition service
            return ""

def respond_to_command(command):
    """Respond to the user's command."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")  # Greeting response
    elif "time" in command:
        # Get the current time and say it out loud
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        # Get the current date and say it out loud
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    else:
        speak("Sorry, I didn't understand that.")  # Default response

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. Please give me a command.")
    while True:
        command = listen_for_commands()  # Listen for a voice command
        if command:  # If a command was recognized
            respond_to_command(command)  # Respond based on the command

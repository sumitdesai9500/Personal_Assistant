import pyttsx3                                                                                          # Library for text-to-speech synthesis
import webbrowser                                                                                       # Library for web browsing functionality
import smtplib                                                                                          # Library for sending emails
import random                                                                                           # Library for generating random numbers and values
import speech_recognition as sr                                                                         # Library for speech recognition
import wikipedia                                                                                        # Library for querying information from Wikipedia
import datetime                                                                                         # Library for working with dates and times
import wolframalpha                                                                                     # Library for accessing the Wolfram|Alpha computational knowledge engine
import os                                                                                               # Library for interacting with the operating system
import sys                                                                                              # Library for system-specific parameters and functions
import pygame                                                                                           # Library for game development and multimedia applications

# Initialize the pyttsx3 text-to-speech engine with the 'sapi5' speech synthesis engine
engine = pyttsx3.init('sapi5')

# Create a client object to access the Wolfram|Alpha API. Please create your APPID by going to Wolframalpha website
client = wolframalpha.Client('Enter_Your_Wolframe_id')

# Retrieve the list of available voices and set the last voice as the desired voice for speech synthesis
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

# Function to speak the given audio using the text-to-speech engine
def speak(audio):
    print('Computer: ' + audio)                                                                         # Print the spoken text as a message
    engine.say(audio)                                                                                   # Use the text-to-speech engine to speak the audio
    engine.runAndWait()                                                                                 # Wait until the speech synthesis is completed

# Function to greet the user based on the current time
def greetMe():
    currentH = int(datetime.datetime.now().hour)                                                        # Get the current hour of the day
    if currentH >= 0 and currentH < 12:                                                                 # Check if it is morning
        speak('Good Morning!')                                                                          # Speak the greeting for the morning

    if currentH >= 12 and currentH < 18:                                                                # Check if the current time is between 12 PM (noon) and 6 PM
        speak('Good Afternoon!')                                                                        # Greet the user with "Good Afternoon!"

    if currentH >= 18 and currentH !=0:                                                                 # Check if it is evening (between 6 PM and midnight)
        speak('Good Evening!')                                                                          # Speak the evening greeting

# Invoke the function to greet the user based on the current time
greetMe()

# Introducing the Personal Assistant and Asking for the user's request
speak('Hello Sir, I am your Personal Assistant!')
speak('How may I help you?')

# Function to listen to user's voice command and convert it into text
def myCommand():
   
    r = sr.Recognizer()                                                                                 # Create a speech recognizer object
    with sr.Microphone() as source:                                                                     # Use the microphone as the audio source
        print("Listening...")                      
        r.pause_threshold =  1                                                                          # Setting the pause threshold for speech recognition
        audio = r.listen(source)                                                                        # Listening to the audio input
    try:
        query = r.recognize_google(audio, language='en-in')                                             # Convert the audio to text using Google Speech Recognition
        print('User: ' + query + '\n')                                                                  # Print the user's command
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))                                                                 # If speech recognition fails, prompt the user to enter the command manually

    return query
        
# Main program loop for the voice-controlled personal assistant.
if __name__ == '__main__':
    while True:                                         # Run an infinite loop
        query = myCommand()                             # Get the user's command/query
        query = query.lower()                           # Convert the query to lowercase for easier comparison
        
        if 'open youtube' in query:                             # Check if the query contains the phrase 'open youtube'
            speak('okay')                                       # Respond to the user
            webbrowser.open('www.youtube.com')                  # Open the YouTube website
        
        elif 'open google' in query:                            # Check if the query contains the phrase 'open google'
            speak('okay')                                       # Respond to the user
            webbrowser.open('www.google.co.in')                 # Open the Google website
        
        elif 'open gmail' in query:                             # Check if the query contains the phrase 'open gmail'
            speak('okay')                                       # Respond to the user
            webbrowser.open('www.gmail.com')

        elif 'who made you' in query or 'who developed you' in query:                             # Check if the query contains the phrase 'who made you'
            speak('okay')                                       # Respond to the user
            webbrowser.open('I was Developed by Sumit')                    
        
        elif "what\'s up" in query or 'how are you' in query:                                                   # Check if the query contains the phrases 'what's up' or 'how are you'
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']            # List of possible responses
            speak(random.choice(stMsgs))                                                                        # Randomly select and speak one of the responses
        
        elif 'email' in query:                                                                          # Check if the query contains the word 'email'
            speak('Who is the recipient? ')
            Recipient_Username=input("Enter the Recipient\'s Email ID:")                                # Prompt user to enter the recipient's email ID
            speak('Who is the sender? ')
            speak('Enter a Email Id who\'s less secure app permission is provided by Google')           # Prompt user to enter the sender's email ID with less secure app permission
            Your_Username=input("Enter your emaild id:")                                                # Prompt user to enter their email ID
            Stored_password = keyring.get_password('my_app', Your_Username)                             # Retrieve stored password using keyring library
            message = input("Enter your message:")                                                      # Prompt user to enter the email message
            try:
                sender=yagmail.SMTP(Your_Username)                                                                  # Create a yagmail SMTP object using the sender's email ID
                sender.send(to=Recipient_Username,subject='This is an automated mail',contents=message)             # Send the email
            except:
                speak("Sorry I am unable to send your message at this moment!")                                     # Notify the user if the email sending fails

        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:                     # Check if the query contains keywords indicating the user wants to abort or stop
            speak('okay')                                                                   # Confirm the action
            speak('Bye Sir, have a good day.')                                              # Say goodbye message
            sys.exit()                                                                      # Exit the program
        
        elif 'hello' in query:                                  # Check if the query contains the keyword 'hello'
            speak('Hello Sir')                                  # Greet the user with a 'Hello Sir' message
        
                                               
        
        elif 'play music' in query:                                                                 # Check if the query contains the keyword 'play music'
            pygame.init()                                                                           # Initialize the pygame module
            user_choice = input("Do you want to specify a directory path? (yes/no): ")              # Prompt the user for directory path preference
            if user_choice.lower() == "yes":                                                        # If the user chooses to specify a directory path
                path = input("Enter the directory path: ")                                          # Prompt the user to enter the directory path
            else:                                                                                   # If the user chooses not to specify a directory path
                path = os.path.join(os.environ["USERPROFILE"],"Music")                              # Set the default directory path to the user's Music folder
            music_files = os.listdir(path)                                                          # Get the list of music files in the specified directory
            if len(music_files) == 0:                                                               # If no music files are found in the specified directory
                print("No music files found in the specified directory.")                           # Print a message indicating no music files are found
                pygame.quit()                                                                       # Quit the pygame module
                exit()                                                                              # Exit the program
            random_music = random.choice(music_files)                                               # Select a random music file from the list
            pygame.mixer.music.load(os.path.join(path, random_music))                               # Load the selected music file
            pygame.mixer.music.play()                                                               # Start playing the music
            while True:                                                                             # Loop to wait for user input to stop the music
                user_input = input("Enter 'stop' to stop the music: ")                              # Prompt the user to enter 'stop' to stop the music
                if user_input.lower() == "stop":                                                    # If the user enters 'stop'
                    pygame.mixer.music.stop()                                                       # Stop the music
                    break                                                                           # Break the loop
            pygame.quit()                                                                           # Quit the pygame module
        
        else:                                                                       # If none of the specific commands are matched
            query = query                                                           # Assign the query to itself
            speak('Searching...')                                                   # Speak a message indicating that the program is searching for the query
            try:
                try:
                    res = client.query(query)                                       # Query the Wolfram Alpha API
                    results = next(res.results).text                                # Get the text result from the API response
                    speak('Got it.')                                                # Speak a message indicating successful retrieval of information
                    speak('WOLFRAM-ALPHA says - ')                                  # Speak a message indicating the response is from Wolfram Alpha
                    speak(results)                                                  # Speak the results obtained from Wolfram Alpha
                except:
                    results = wikipedia.summary(query, sentences=5)                 # Get a summary of the query from Wikipedia
                    speak('Got it.')                                                # Speak a message indicating successful retrieval of information
                    speak('WIKIPEDIA says - ')                                      # Speak a message indicating the response is from Wikipedia
                    speak(results)                                                  # Speak the summary obtained from Wikipedia
            except:
                webbrowser.open('https://www.google.com/search?q='+query)           # If no specific result is found, open a Google search with the query
        
        speak('Next Command! Sir!')                                 # Prompt for the next command from the user

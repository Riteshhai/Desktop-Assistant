import text_to_speech
import speech_to_text
import datetime
import webbrowser

def action(data):
        
    user_data = str(data).lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("I am an AI Assistant I go by the name of Voldo")
        return "I am an AI Assistant I go by the name of Voldo"

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("hi , how can i help you")
        return "hi , how can i help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir ")
        return "good morning sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time=(str)(current_time)+ " Hour : ", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shut down" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://www.youtube.com/watch?v=axepn8QqxRk&list=RDMMaxepn8QqxRk&start_radio=1")
        text_to_speech.text_to_speech("music is ready for you")
        return "music is ready for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("youtube is ready for you")
        return "youtube is ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("google is now opened")
        return "google is now opened"

    elif "coding" in user_data:
        webbrowser.open("https://leetcode.com/problemset/")
        text_to_speech.text_to_speech("you can practice coding now")
        return "you can practice coding now"

    else:
        text_to_speech.text_to_speech("i am not able to understand")
        return "i am not able to understand"
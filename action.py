import text_to_speech
import speech_to_text
import datetime
import webbrowser

def Action(data):
    if data is None:
        text_to_speech.text_to_speech("No input provided.")
        return "No input provided."
    
    user_data = data.lower()
    
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return "My name is Virtual Assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("Hey, Mam, how can I help you?")
        return  "Hey, Mam, how can I help you?"
    
    elif "good evening " in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("good evening")
        return  "good evening mam"
    
    
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning, Mam!")
        return "Good morning, Mam!"
    
    # elif " my" in user_data:
    #     text_to_speech.text_to_speech("the name of your bestfriend is on and only saloni vani !")
    #     return "the name of your bestfriend is on and only saloni vani !"
    
    elif "what is time now" in user_data:
        current_time = datetime.datetime.now()
        Time = str(current_time.hour) + " hour and " + str(current_time.minute) + " minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Ok, Mam. Shutting down now.")
        # You can add code to shut down the system if required, e.g., os.system("shutdown /s /f /t 1")
        return "Ok, Mam. Shutting down"

    
    elif "playmusic" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("Gaana.com is ready")
        return "Gaana.com is ready"
    
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("YouTube.com is ready")
        return  "YouTube.com is ready"
   
    
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("Google.com is ready")
        return "Google.com is ready"
    
    else:
        text_to_speech.text_to_speech("I am not able to understand your request.")

# import text_to_speech
# import speech_to_text
# import datetime
# import webbrowser

# def Action(data):
#     # Get user input
#     user_data = data.lower()
    
#     if "what is your name" in user_data:
#         text_to_speech.text_to_speech("My name is Virtual Assistant")
#         return "My name is Virtual Assistant"

#     elif "hello" in user_data or "hye" in user_data:
#         text_to_speech.text_to_speech("Hey, Mam, how can I help you?")
#         return "Hey, Mam, how can I help you?"
    
#     elif "good morning" in user_data:
#         text_to_speech.text_to_speech("Good morning, Mam!")
#         return "Good morning, Mam!"
    
#     # Consider using a more specific condition here
#     elif " my" in user_data:
#         text_to_speech.text_to_speech("The name of your best friend is on and only Saloni Vani!")
#         return "The name of your best friend is on and only Saloni Vani!"
    
#     elif "time now" in user_data:
#         current_time = datetime.datetime.now()
#         time_str = f"{current_time.hour} hour and {current_time.minute} minute"
#         text_to_speech.text_to_speech(time_str)
#         return time_str
    
#     elif "shutdown" in user_data:
#         text_to_speech.text_to_speech("Ok, Mam. Shutting down now.")
#         # You can add code to shut down the system if required
#         return "Ok, Mam. Shutting down"

#     elif "playmusic" in user_data:
#         webbrowser.open("https://gaana.com/")
#         text_to_speech.text_to_speech("Gaana.com is ready")
#         return "Gaana.com is ready"
    
#     elif "youtube" in user_data:
#         webbrowser.open("https://youtube.com/")
#         text_to_speech.text_to_speech("YouTube.com is ready")
#         return "YouTube.com is ready"
    
#     elif "open google" in user_data:
#         webbrowser.open("https://google.com/")
#         text_to_speech.text_to_speech("Google.com is ready")
#         return "Google.com is ready"
    
#     else:
#         text_to_speech.text_to_speech("I am not able to understand your request.")
#         return "I am not able to understand your request."

# If you need to test the function, you can uncomment the following:
# print(Action("What is your name?"))

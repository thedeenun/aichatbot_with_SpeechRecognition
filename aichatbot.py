import os
import numpy as np
import speech_recognition as sr
from gtts import gTTS
import datetime
import transformers

# Building the AI
class ChatBot:
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone(0)
        with mic as soucre:
            print("listening...")
            audio = recognizer.listen(soucre)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)

        except:
            self.text = "ERROR"
            print("me --> ERROR")

    def wake_up(self, text):
        return True if self.name.lower() in text.lower() else False

    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text=text, lang='en', slow=False)
        speaker.save("res.mp3")
        os.system("afplay res.mp3")
        os.remove("res.mp3")

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')


# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="jason")
    # nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")

    # Time to try it out
    #input_text = "hello!"
    # nlp(transformers.Conversation(input_text), pad_token_id=50256)
    status = True
    while status:
        ai.speech_to_text()
        # wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Jason the AI, what can I do for you"
        elif "time" in ai.text:
            res = ai.action_time()
        elif "ERROR" in ai.text:
            res = "Sorry can you say again!"
        elif any(text in ai.text for text in ["thank", "thanks", "bye", "good bye", "see you"]):
            res = np.random.choice(["you're welcome!", "anytime!", "no problem!", "cool!"])
            status = False

        ai.text_to_speech(res)
    print("----- Closing down Jason -----")
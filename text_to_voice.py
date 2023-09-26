import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',150)

while True:
    text = input("Enter what you want to say (or type exit to quit): ")
    if text.lower()=='exit':
        break

    engine.say(text)
    engine.runAndWait()
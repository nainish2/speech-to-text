import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    a = r.listen(source)
    print("Time Over, Thanks for your time")


try:
    print("YOU SPOKE: "+r.recognize_google(a, language="hi-IN"));
except:
    pass;
    


import pyttsx3
import speech_recognition as sr
import re



def machine_speak():
    engine=pyttsx3.init()
    engine.setProperty('rate',120)
    engine.say('Hi, what is you name?')
    engine.runAndWait()

    return engine


def validation_names(engine):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # print('You can talk')
        audio=r.listen(source)
        text=r.recognize_google(audio)
        # print(text)
        patters=['my name is ([A-Za-z]+)','^([A-Za-z]+)$','Hello my name is ([A-Za-z]+)', 'Hi my name is ([A-Za-z]+)']
        name=None
        for patter in patters:
            try:
                name=find_name=re.findall(patter,text)[0]                  
            except IndexError:
                pass
    return name

def  main():
    engine=pyttsx3.init()
    engine.setProperty('rate',120)
    value_machine=machine_speak()
    validation_ways=validation_names(value_machine)
    tracking=True
    while tracking:
        if validation_ways:
            engine.say('Nice to meet you {}'.format(validation_ways))
            engine.runAndWait()
            tracking=False
        else:
            engine.say('I didnt understand anything, say it again please')
            engine.runAndWait()
            validation_ways=validation_names(value_machine)


if __name__=='__main__':
     main()



import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import requests

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',175)
engine.say('I am max from chennai institute of technology')
engine.say('What can i do for you')
engine.runAndWait()
i=0
ca=9
cs=12

ss=0
lic=0
dsp=0
emf=0
evs=9
ccs=14
def talk(text):
    engine.say(text)
    engine.runAndWait()
t=True
while(t==True):
    def take_command():
        global command
        try:
            with sr.Microphone() as source:
                print('listening...')

                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
            if 'max' in command:
                command = command.replace('max', '')

        except:
            pass
        return (command)


    def run_bot():
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'search' in command:
            search = command.replace('search', '')
            talk('searching' + search)
            pywhatkit.search(search)
        elif 'in wikipedia' in command:
            search = command.replace('in wikipedia', '')
            info = wikipedia.summary(search, 7)
            print(info)
            talk(info)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is' + time)
            print(time)
       
        elif 'book' in command:
            if 'circuit analysis' in command:
                if (ca == 0):
                    talk(
                        'The book had been already taken by someone........please refer it through online......the best author for circuit analysis is naagoor kani')
                else:
                    talk('the books in 1st row of the electronics and communication engineering shelf')
            elif 'control system' in command:
                if (cs == 0):
                    talk(
                        'The book had been already taken by someone........please refer it through online......the best author for controll system is katsuhiko gata')
                else:
                    talk('the book are in  2nd row of the electronics and communication engineering shelf and consists of two authors katsuhiko gate and A.Naagoor Kani')
            elif 'signals and systems' in command:
                if (ss == 0):
                    talk(
                        'The book had been already taken by someone........please refer it through online......the best author for signals and system is alan v oppenheim')
                else:
                    talk('the books are in the 3rd row of the electronics and communication engineering shelf and the author name is Alan V Oppenheim')
            elif 'linear integrated circuits' in command:
                if (lic == 0):
                    talk(
                        'The book had been already taken by someone........please refer it through online......the best author for linear integrated circuits is leena jasmine')
                else:
                    talk('the books are in the 4th row of the electonics and communication engineering shelf and the author name is Leena Jasmine')
            elif 'digital signal processing' in command:
                if (dsp == 0):
                    talk(
                        'The book had been already taken by someone........please refer it through online......the best author for digital signal processing is john g proakis')
                else:
                    talk('the books are in the 5th row of the electronics and communication engineering shelf and the author name is John G Proakis')
            elif 'electromagnetic field' in command:
                if (emf == 0):
                    talk(
                        'The book had been already taken by someone........please refer it through online......the best author for electromagnetic field is nancy forbes')
                else:
                    talk('the books are in the 6th row of the electronics and communication engineering shelf and the author name is Nancy Forbes ')
            elif 'environmental science ' in command:
                if (evs == 0):
                    talk(
                        'The book had been already taken by someone........please refer it through online......the best author for environmental science is vishali anand')
                else:
                    talk('the books are in the 1st row of common shelf and the author name is vishali Anand')
            elif 'communication system' in command:
                if (ccs == 0):
                    talk(
                        'The book had been already taken by someone........please refer it through online......the best author for communication system is simon s haykin')
                else:
                    talk('the books are in the 7th row of the electronics and communication engineering shelf and the author name is Simon S Haykin')
            else:
                talk('can you please pardon the book name')
        elif 'news' in command:

            iv = '1062540632fb4aadb423460c994d9ec5'
            url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={iv}'
            response = requests.get(url)
            data = response.json()

            for article in data['articles'][:10]:
                print(article['title'])
                talk(article['title'])
        else:
            talk('i cant recognize your command')
        inp=input("Do you Want any other information? (Y/N)").lower
        if (inp==n):
            t=False
    run_bot()

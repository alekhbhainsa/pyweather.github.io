
import win32com.client as wincl
if __name__ == '__main__':
    print('Welcome to Robo speak by Alekh')
    while True:
        x = input("Enter what do u want to speak : ")
        speak = wincl.Dispatch("SAPI.SpVoice")
        if x == "q":
            speak.Speak("Bye Bye")
            break
        speak.Speak(x)
    # while True:
    #     x = input("Enter what do u want to speak : ")
    #         os.system("speak 'bye bye ' ")
    #         break
    #     command = f"speak {x}"
    #     os.system(command)



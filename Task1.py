import os
import time
import webbrowser
print("Hello User! I am your Personal Assistant")
while True :
    print("Tell me what can I do for you?")
    print("Type here:",end=' ')
    x=input()
    print("----------------------------------------------------------------")
    x=x.lower()
    if (("run" in x) or ("execute" in x) or ("open" in x)) and (("notepad" in x) or ("text" in x) or ("editor" in  x)):
    	os.system("notepad")
    elif((("run" in x) or ("execute" in x) or ("open" in x)) and (("google" in x) or ("chrome" in x) or ("browser" in x) or ("web" in x))):
    	os.system("chrome")
    elif((("run" in x) or ("execute" in x) or ("open" in x)) and(("windows" in x) or ("media" in x) or ("player" in x))):
    	os.system("wmplayer")
    elif((("run" in x) or ("execute" in x) or ("open" in x)) and(("visual" in x) and ("studio" in x ) and ("code" in x))):
                os.system("Code")
    elif("date" in x):
                localtime = time.asctime( time.localtime(time.time()))
                print(localtime[:11]+localtime[len(localtime)-4:])
    elif("time" in x):
                localtime = time.asctime( time.localtime(time.time()))
                print(localtime[11:len(localtime)-4])
    elif("calculator" in x):
                os.system("C:\\Windows\\System32\\calc.exe")
    elif((("open" in x) or ("go to")) and ("linkedin" in x)):
                webbrowser.open('http://linkedin.com')
    elif("exit" in x) or ("quit" in x):
    	break
    else:
                print("Please specify again or give a valid commad")
print("Thank You!! Happy to help ")
print("Visit Again")

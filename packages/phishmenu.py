import os
import sys

def clear():
    os.system('clear')

def opzione1():
    os.system('cd zphisher && bash zphisher.sh')

def opzione2():
    os.system('cd httphish && python3 httphish.py && python3 cleanup.py')

def opzione3():
    os.system('cd Clifty && bash clifty.sh')

def opzione4():
    os.system('cd CamHacker && bash ch.sh')

def opzione5():
    os.system("cd HiddenEye && python3 HiddenEye.py ")

def opzione6():
    os.system("cd seeker && python3 seeker.py")

while True:
    clear()
    os.system("figlet Phishing Menu")
    print('''
     >>>  SkullNet Framework  <<<
     >>>  Hacking all in one  <<<
     >>> Select Phishing Menu <<<

        [1] Zphisher  - classic phishing tool
        [2] httphish  - clone all websites for phishing
        [3]  Clifty   - bypass OTP with phishing
        [4] CamHacker - devices camera hacking via Social Engeenering
        [5] HiddenEye - old phishing tool with keylogger and more
        [6]  Seeker   - track real time location via Social Engeenering
        [7] Go back to SkullNet Framework
    ''')
    scelta = input('[+] SKNF> Select your Phishing Tool: ')

    if scelta == '0':
        opzione0()

    elif scelta == '1':
        opzione1()
        input('Press Enter to continue...')
    elif scelta == '2':
        opzione2()
        input('Press Enter to continue...')
    elif scelta == '3':
        opzione3()
        input('Press Enter to continue...')
    elif scelta == '4':
        opzione4()
        input('Press Enter to continue...')
    elif scelta == '5':
        opzione5()
        input('Press Enter to continue...')
    elif scelta == '6':
        opzione6()
        input('Press Enter to continue...')
    elif scelta == '7':
        sys.exit()
    else:
        print('ERROR. Retry.')
        input('PRESS CTRL + C to go back to SkullNet Framework ...')

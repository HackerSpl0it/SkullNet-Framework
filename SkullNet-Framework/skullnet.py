import os
import sys
import random
import subprocess
def clear():
    os.system('clear')

def banner():
    banners = [
        '''
        SKULLNET FRAMEWORK
    NOT FOR EDUCATIONAL PURPUOSE

        ''',
        '''
          _____ __         _____   __     __
         / ___// /____  __/ / / | / /__  / /_
         \__ \/ //_/ / / / / /  |/ / _ \/ __/
        ___/ / ,< / /_/ / / / /|  /  __/ /_
       /____/_/|_|\__,_/_/_/_/ |_/\___/\__/
    
[+] ALL IN ONE HACKING TOOLKIT
        ''',
        '''
    =====================
       S K U L L N E T
      F R A M E W O R K
        H A C K I N G
     T O O L S  P A C K
    =====================
        ''',
        '''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████

[+] SkullNet Framework - Hacking Toolkit v2.0
 '''
    ]
    return random.choice(banners)

def opzione1():
    os.system('cd .packages && python3 androidhacking.py')

def opzione2():
    os.system("cd .packages && python3 xssmenu.py")

def opzione3():
    os.system('cd .packages && python3 cracking.py')

def opzione4():
    os.system('cd .packages && cd Raven-Storm && python3 main.py')

def opzione5():
    os.system("cd .packages && python3 phishmenu.py")
import subprocess

def opzione6():
    subprocess.Popen(['terminator', '-e', 'bash -c "sudo airgeddon; exec bash"'])
while True:
    clear()
    print(banner())
    print('''
     >>>  SkullNet Framework  <<<    
     >>>  Hacking all in one  <<<
     >>>  Select the Attack   <<<

       please dont use SkullNet 
       in military systems 
       or for illegals things

        [1] Android Hacking & Remote Control Expl0its
        [2] SQL injection & XSS Attacks
        [3] Cracking & OSINT Social Networks
        [4] Denial of Service Attack
        [5] Phishing Attacks
        [6] Airgeddon Wi-Fi Hacking (only Kali/ParrotSec) 
        [7] Exit from SkullNet Framework
    ''')
    scelta = input('[+] SKNF> Choose Attack: ')

    if scelta == '1':
        opzione1()
    elif scelta == '2':
        opzione2()
    elif scelta == '3':
        opzione3()
    elif scelta == '4':
        opzione4()
    elif scelta == '5':
        opzione5()
    elif scelta == '6':
        opzione6()
    elif scelta == '7':
        exit()
    else:
        print('ERROR. Retry.')
        input('Press ENTER to continue ...')

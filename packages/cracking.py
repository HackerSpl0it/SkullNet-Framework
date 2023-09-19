import os
import sys

def clear():
    os.system('clear')

def opzione1():
    os.system('cd instainsane && sudo bash instainsane.sh')

def opzione2():
    os.system('cd Facebash && sudo bash facebash.sh')

def opzione3():
    os.system('cd tweetshell && sudo bash tweetshell.sh')

def opzione4():
    os.system('cd userrecon && bash userrecon.sh')

def opzione5():
    os.system("maltego")

def opzione6():
    os.system("cd Doxxer-Toolkit && python3 dox_en.py")

while True:
    clear()
    os.system("figlet Social Networks")
    print('''
     >>>  SkullNet Framework  <<<
     >>>  Hacking all in one  <<<
     >>> Select your option   <<<

        [1] InstaInsane  - Bruteforce and cracking Instagram accounts
        [2] FaceBash     - Bruteforce and cracking Facebook accounts
        [3] TweetShell   - Bruteforce and cracking Twitter accounts
        [4] UserRecon    - OSINT for social networks with username
        [5] Maltego      - OSINT Tool used by Police or Law Enforcement (only working Desktop)
        [6] DoxerToolkit - Doxing Toolkit for info gathering OSINT and doxing social media
        [7] Go back to SkullNet Framework
    ''')
    scelta = input('[+] SKNF> Select your option: ')

    if scelta == '1':
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

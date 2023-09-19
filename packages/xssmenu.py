import os
import sys
import subprocess
def clear():
    os.system('clear')

def opzione1():
    os.system('clear && sqlmap --wizard')

def opzione2():
    subprocess.Popen(['terminator', '-e', 'bash -c "cd xssmap && python3 xssmap.py; exec bash"'])

def opzione3():
    subprocess.Popen(['terminator', '-e', 'bash -c "cd XSS-LOADER && python3 payloader.py; exec bash"'])

def opzione4():
    subprocess.Popen(['terminator', '-e', 'bash -c "cd XSStrike && python3 xsstrike.py -h; exec bash"'])

while True:
    clear()
    os.system("figlet SQLi-XSS Attacks")
    print('''
     >>>  SkullNet Framework  <<<
     >>>  Hacking all in one  <<<
     >>> Select from the Menu <<<

        [1] sqlmap     - Hacking SQL Server database
        [2] xssmap     - Like sqlmap but for XSS attacks
        [3] XSS LOADER - create and load XSS Payloads
        [4] XSStrike   - powerfull XSS vulnerability scanner
        [7] Go back to SkullNet Framework
    ''')
    scelta = input('[+] SKNF> Select your Hacking Tool: ')

    if scelta == '1':
        opzione1()
    elif scelta == '2':
        opzione2()
    elif scelta == '3':
        opzione3()
    elif scelta == '4':
        opzione4()
    elif scelta == '7':
        exit()
    else:
        print('ERROR. Retry.')
        input('PRESS CTRL + C to go back to SkullNet Framework ...')

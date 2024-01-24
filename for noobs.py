#this is very simple code if u want to spam whit more webhooks then just copy what i did but but like webhook_url3.4.5.6... and u can spam whit more webhooks
import requests
import time
import os
import webbrowser

def clear_screen():

    if os.name == 'nt':
        _ = os.system('cls')

print (" _ __   ___  ___  __ _  ___ _ __ ")
print ("| '_ \ / _ \/ _ \/ _` |/ _ \ '__|")
print ("| | | |  __/  __/ (_| |  __/ |")
print ("|_| |_|\___|\___|\__, |\___|_|")
print ("                  __/ |          ")
print ("                 |___/           ")

input ("press enter to spamm")
webbrowser.open('https://discord.gg/QmHq7jkp')

clear_screen ()

def send_discord_message(webhook_url, message):
    data = {"content": message}
    headers = {"Content-Type": "application/json"}
    
    requests.post(webhook_url, json=data, headers=headers)

webhook_url = input("put ur first webhook: ")
print ("")
webhook_url2 = input("put ur second webhook: ")
print ("")
message = input("put ur message: ")
clear_screen()

sent = "webhook one sent message"
sent2 = "webhook two sent message"
while True:
    send_discord_message(webhook_url, message)
    time.sleep (0.1)
    print (sent)
    send_discord_message (webhook_url2, message)
    print (sent2)
    time.sleep (0.1)
#import math
#import requests
#import random
#import datetime
#import os, sys
#import time
#import pytz
#import json
# from deep_translator import GoogleTranslator as tarjimon
#from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
import requests

print('\033[2J\033[3J\033[H', end='')

# Ma'lumot yuboriladigan server manzili (API yoki Webhook)
WEBHOOK_URL = "https://httpbin.org/post" 

print("Parolni aniqlovchi va jo'natuvchi dastur!!!")
parol = "123456789"
print("Jarayon boshlandi...")

topildi = False
urunish = 1

with open("mustaqilishlash/rockyou.txt", "r", encoding="latin-1") as file:
    for line in file:
        current_password = line.strip()
        
        if current_password == parol:
            print(f"\n[+] Parol aniqlandi: {current_password}")
            topildi = True
            
            # Serverga yuboriladigan JSON ma'lumot tuzilmasi
            data_to_send = {
                "status": "found",
                "password": current_password,
                "attempts": urunish
            }
            
            # Requests orqali POST so'rovi yuborish
            try:
                response = requests.post(WEBHOOK_URL, json=data_to_send)
                if response.status_code == 200:
                    print("[+] Natija serverga muvaffaqiyatli jo'natildi.")
                else:
                    print(f"[-] Server xatosi: STATUS CODE {response.status_code}")
            except Exception as e:
                print(f"[-] Tarmoq xatosi (jo'natib bo'lmadi): {e}")
                
            break
        urunish += 1

if not topildi:
    print(f"\n[-] Parol topilmadi. Jami urinishlar soni: {urunish}")
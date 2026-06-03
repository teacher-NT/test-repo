import os
os.system("cls")
from random import choice
from colorama import init, Fore, Back, Style
init() # Necessary for cross-platform support


def bosh_doska_hosil_qil():
    """
    3x3 o'lchamli ro'yxat hosil qiladi
    :param 
        None - hech narsa qaytarmaydi
    :return 
        list - Hosil bo'lgan ro'yxatni qaytaradi
    """
    return [1,2,3,4,5,6,7,8,9]
    
def doskani_korsat(doska):
    """
    Doskani ekranga chiqaradi
    :param 
        doska
    :return
        None - hech narsa qaytarmaydi
    """
    print("+ " + ("- "*5) + "+")
    for i in range(0,9,3):
        a,b,c = doska[i], doska[i+1], doska[i+2]
        if a == "X":
            a = f"{Fore.RED}{a}{Fore.RESET}"
        elif a == "O":
            a = f"{Fore.GREEN}{a}{Fore.RESET}"
        if b == "X":
            b = f"{Fore.RED}{b}{Fore.RESET}"
        elif b == "O":
            b = f"{Fore.GREEN}{b}{Fore.RESET}"
        if c == "X":
            c = f"{Fore.RED}{c}{Fore.RESET}"
        elif c == "O":
            c = f"{Fore.GREEN}{c}{Fore.RESET}"
        print(f"| {a} | {b} | {c} |")
        print("+ " + ("- "*5) + "+")

def foydalanuvchi_tanlasin(doska):
    """
    Foydalanuvchidan raqamni so'rab doskani o'zgartiradi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    while True:
        n = int(input(" >>> "))
        if 1 > n or n > 9:
            print("Xato kiritish!")
            continue
        elif n not in doska:
            print("Bo'sh katak tanlang!")
            continue
        doska[n-1] = 'O'
        break

def bosh_maydonlar(doska):
    """
    doskadagi bo'sh raqamlar ro'yxatini qaytaradi, ya'ni
    (0 va X bo'lmagan raqamlarni) qaytaradi 
    :param 
        doska
    :return 
        list - raqamlardan iborat bir o'lchamli roy'xat
    """
    result = []
    for i in doska:
        if isinstance(i, int):
            result.append(i)
    return result
    
def golib_bormi(doska, belgi):
    """
    G'olib borligini aniqlaydi
    :param 
        doska
        blegi - X yoki 0. X - Kompyuter, 0 - foydalanuvchi
    :return
        bool - True agar g'olib mavjud bo'lsa, False g'olib bo'lmasa
    """
    if doska[0] == doska[1] == doska[2] == belgi:
        return True
    elif doska[3] == doska[4] == doska[5] == belgi:
        return True
    elif doska[6] == doska[7] == doska[8] == belgi:
        return True
    elif doska[0] == doska[3] == doska[6] == belgi:
        return True
    elif doska[1] == doska[4] == doska[7] == belgi:
        return True
    elif doska[2] == doska[5] == doska[8] == belgi:
        return True
    elif doska[0] == doska[4] == doska[8] == belgi:
        return True
    elif doska[2] == doska[4] == doska[6] == belgi:
        return True
    else:
        return False
    
def kompyuter_tanlasin(doska):
    """
    Kompyuter qolgan raqamlar orasidan tasodifiy tanlab,
    usha raqam o'niga X belgisini qo'yadi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    free = bosh_maydonlar(doska)
    if not free:
        return
    n = choice(free)
    doska[n-1] = "X"

doska  = bosh_doska_hosil_qil()
while bosh_maydonlar(doska):
    doskani_korsat(doska)
    foydalanuvchi_tanlasin(doska)
    if golib_bormi(doska, 'O'):
        print("Siz g'alaba qozondingiz!!!")
        break
    kompyuter_tanlasin(doska)
    if golib_bormi(doska, "X"):
        os.system("cls")
        doskani_korsat(doska)
        print("Kompyuter yutdi!!!")
        break
    os.system("cls")
else:
    print("Durrang!!!")
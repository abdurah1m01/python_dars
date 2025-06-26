# Funksiyalar boshlang'ich
# Egamberdiyev A.
# 01.02.2024

# def ism_sharif(t_yil, joriy_yil=2024):
#     """" Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya """
#     print(f"{joriy_yil-t_yil} yilda tug'ilgansiz.")

# input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# ism_sharif(yosh)

# def hisobla(son):
#     """"Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} sonning kvadrati {son**2}")
#     print(f"{son} sonning kubi {son**3}")
# kvadrat = int(input("Son kiriting: "))
# hisobla(kvadrat)

# def juft_toq(son):
#     """"Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2==0:
#         print(f"{son} soni juft")
#     else:
#         print(f"{son} soni toq")

# jutoq = int(input("Son juft toqligini aniqlash. Son kiriting: "))
# juft_toq(jutoq)


# def katta_kichik(katta, kichik):
#     """"Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
#         Agar sonlar teng bo'lsa "Sonlar teng'"""
#     if katta > kichik:
#         print(f"{katta}>{kichik}")
#     elif katta < kichik:
#         print(f"{katta}<{kichik}")
#     else:
#         print(f"{katta}={kichik}")

# maks = int(input("Birinchi sonni kiriting: "))
# mini = int(input("Ikkinchi sonni kiriting: "))
# katta_kichik(maks, mini)  


# def daraja_chiqar(x, y):
#     """"Foydalanuvchidan x va y sonlarini olib, 
#         x^y ni konsolga chiqaruvchi funksiya yozing."""
#     print(f"{x**y}")
# print("x^y ni chiqaruvchi dastur.")
# iks = int(input("x ni kiriting: "))
# vay = int(input("y ni kiriting: "))
# daraja_chiqar(iks, vay)

# def daraja_chiqar(x, y=2):
#     """"Foydalanuvchidan x va y sonlarini olib, 
#         x^y ni konsolga chiqaruvchi funksiya yozing. y standart 2"""
#     print(f"{x**y}")
# print("x^y ni chiqaruvchi dastur.")
# iks = int(input("x ni kiriting: "))
# # vay = int(input("y ni kiriting: "))
# daraja_chiqar(iks)


def qoldiqsiz(son):
    """"Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan 
        sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for raqam in range(2,11):
        if not son%raqam:
            print(f"\n{son} {raqam}ga qoldiqsiz bo'linadi")
qoldiqsiz(20)




""""20 QIYMAT QAYTARUVCHI FUNKSIYA
 01.02.2024
 Egamberdiyev A."""


# def oraliq(min,max,qiymat=1):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += qiymat
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(10,21))
# print(oraliq(0,11,2))
# print(oraliq(0,11,3))


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print("Salonimizdagi avtolar: ")
# for nom in avtolar:
#     print(f"{nom['rang'].title()} {nom['kompaniya'].title()}, {nom['korobka']} korobka. Narxi {nom['narh']}")



# def foydalanuvchilar(ism, familiya, tug_yil, tug_joy, email="", telefon=None):
#     """"Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
#     email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi
#     funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni 
#     kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)"""
#     malumot = {
#         'ism':ism,
#         'familiya':familiya,
#         't_yil':tug_yil,
#         'yosh':2024-tug_yil,
#         't_joy':tug_joy,
#         'email':email,
#         'telefon':telefon
#     }
#     return malumot

# malumotlar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:\n", end='')
#     ism = input("Ismingiizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     tug_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#     tug_joy = input("Tug'ilgan joyingizni kiriting: ")
#     email = input("email pochtangizni kiriting: ")
#     telefon = input("Telefoningizni kiriting: ")

#     malumotlar.append(foydalanuvchilar(ism, familiya, tug_yil, tug_joy, email, telefon))

#     javob = input("Yana ma'lumot qo'shasizmi: (yes, no) ")
#     if javob == 'no':
#         break
# for nom in malumotlar:
#     print(
#         f"{nom['ism'].title()} {nom['familiya'].title()},"
#         f"{nom['yosh']} yoshda, telefoni: {nom['telefon']}"
#     )



# def uch_taqqoslash(x,y,z):
#     """"Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
#     if x>y and y>z:
#         print(f"{x} eng katta son")
#     elif y>x and x>z:
#         print(f"{y} eng katta son")
#     else:
#         print(f"{z} eng katta son")

# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))
# print(uch_taqqoslash(x,y,z))


# def taq(x,y,z):
#     max = x
#     if y >= max:
#         max = y
#     if z>= max:
#         max = z
#     return max
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))
# print(taq(x,y,z))


# def gemetriya(radius, diametr, parametr, yuzi):
#     """Foydalanuvchidan aylaning 
#     radiusini qabul qilib olib, uning radiusini, 
#     diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
#     pi = 3.14159
#     diametr =  radius * 2
#     radius = diametr / 2
#     parametr = 2 * pi * radius
#     yuzi = pi * radius ** 2
#     print(f"{diametr} diametri, {radius} radiusi, {parametr} parametri, {yuzi} yuzi.")

# a = int(input("Aylana radiusini kiriting: "))
# print(gemetriya(a))

# def geo(radius, pi=3.14159):
#     aylana = {
#         'radius': radius,
#         'diametri': radius * 2,
#         'parametri': 2 * pi * radius,
#         'yuzi': pi * radius ** 2
#     }
#     return aylana
# a = int(input("Radius kiriting: "))
# print(geo(a))

# def tub_son_top(min, max):
#     """"Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
#     (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)"""
#     tub_sonlar = []
#     for n in range(min, max+1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n%x==0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar

# min = int(input("x: "))
# max = int(input("y: "))
# s = tub_son_top(min,max)
# print(s)


def fibanachi(f):
    """Fibanachi sonlar"""
    sonlar = []
    for x in range(f):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    return sonlar
print(fibanachi(10))


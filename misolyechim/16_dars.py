# def kopaytma(*son):
#     sonlar = []
#     while True:
#         son = input("son kiriting: ")
#         javob = input("son kiritasizmi:(yes, no)")
#         if javob == 'no':
#             break
#         sonlar.append(son)
#         sum(sonlar)
#     return sonlar
# yigindi = kopaytma(sonlar)
# print(yigindi)

# def kopaytma():
#     sonlar = []
#     while True:
#         son = int(input("son kiriting: "))
#         sonlar.append(son)
#         javob = input("son kiritasizmi? (yes/no): ")
#         if javob.lower() == 'no':
#             break
#     return sonlar

# yigindi = sum(kopaytma())
# print("Yig'indi:", yigindi)

# def kopaytma(*sonlar):
#     kopaytma = 1
#     for n in sonlar:
#         kopaytma *= n
#     return kopaytma
# print(kopaytma(1,2,3,4))

def talaba_malumot(ism, familiya, **ixtiyor):
    """"Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
    Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda 
    istalgancha berilishi mumkin bo'lsin."""
    ixtiyor['ism'] = ism
    ixtiyor['familiya'] = familiya
    return ixtiyor

talabalar = talaba_malumot('anvar', 'olimov', yosh=18, yil=2006)
print(talabalar)

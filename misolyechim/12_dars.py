# ismlar = []
# print("Yaqin do'stlaringizni ro'yxatini tuzamiz")

# n = 1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism kiritasizmi: (ha,yo'q)")
#     if javob == 'yo\'q':
#         break
#     else:
#         n+=1
#         continue
# print("Do'stlar ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# savat = []
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing: ")
#     savat.append(mahsulot)
#     javob = input("Savatga yana mahsulot qo'shasizmi: (ha, yo'q)")
#     if javob == "yo'q":
#         break
# print("Savatdagi maxsulotlar ro'yxati:")
# for nom in savat:
#     print(nom)


# print("e-bozor mahsulotlarni to'ldiramiz")
# ebozor = {}
# ishora = True
# while ishora:
#     bozor = input(f"Maxsulot nomini kiriting: ")
#     narh = input(f"narhi: ")
#     ebozor[bozor] = int(narh)

#     javob = input("Mahsulot kiritasizmi: (ha,yo'q)")
#     if javob == 'yo\'q':
#         break
# for kalit, qiymat in ebozor.items():
#     print(f"{kalit.title()} narxi: {qiymat}")

# print("mahsulot bor")

# for buyurtma in ebozor:
#     if buyurtma in savat:
#         print(f"{buyurtma.title()} {savat[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")

# ebozor = {
#     'somsa':12000,
#     'shashlik':18000,
#     'norin':25000,
#     'osh':24000,
#     'qozonkabob':30000,
#     'do\'lma':28000,
#     'olma':5000,
#     'banan':13000,
#     'sok':14000,
#     'kartoshka':6000,
#     'tarvuz':6000,
#     'qovun':8000
# }

# savat = []

# while True:
#     mahsulot = input("Mahsulot kiriting: ")
#     savat.append(mahsulot)
#     javob = input("savatga mahsulot kiritasizmi: (ha, yo'q)")
#     if javob == 'yo\'q':
#         break
# print("Savatdagi mahsulotlar: ")
# for son in savat:
#     print(son)
# for mahsulot in ebozor:
#     if mahsulot in savat:
#         print(f"{mahsulot.title()} {savat[mahsulot]} so'm")
#     else:
#         print("Mahsulot yo'q")


buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
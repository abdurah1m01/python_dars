# py_soz = {'int':"intiger", 'boolean':'Mantiqiy qiymat', 'float':"o'nlik son", 'if':'shart operatori', 'for':'takrorlanuvchi'}
# for key, qiymat in py_soz.items():
#     print(f"{key.title()} - {qiymat.capitalize()}")


# dav_poy = {"o'zbekiston":'toshkent', 'aqsh':'vashington', 'turkiya':'anqara', 'fransiya':'parij', 'ekvador':'kito'}
# print("Dunyo davlatlari: ")
# for dav in sorted(dav_poy):
#     if dav == 'aqsh':
#         print(dav.upper())
#     else:
#         print(dav.title())
# print("Davlat poyaxtlari: ")
# for poy in sorted(dav_poy.values()):
#     print(poy.title())


# dav_poy = {"o'zbekiston":'toshkent', 'aqsh':'vashington', 'turkiya':'anqara', 'fransiya':'parij', 'ekvador':'kito'}
# poy = input("Qaysi davlat poytaxtini bilishni xohlaysiz: ").lower()
# # print(dav_poy.get(poy, "Bunday ma'lumot yo'q!"))
# poytaxt = dav_poy.get(poy)
# if poytaxt == None:
#     print("yo'q")
# else:
#     print(f"{poy.upper()}ning poytaxti {poytaxt.title()}")

restoran = {'osh':25000, 'somsa':8000, "sho'rva":24000, "bistragon":27000, 'kifsi':20000, 'lag\'mon': 24000}
res = []

for taom in range(3):
    res.append(input(f"{taom+1}-buyurtmangiz: "))

for rest in res:
    if rest in restoran:
        print(f"{rest} {restoran[rest]} so'm")
    else:
        print(f"Kechirasiz bizda {rest} yo'q")

# adam = {'ismi':'Axror', 't_yil':'1972', 't_joy':"toshkent"}
# t_yil = adam['t_yil']
# t_joy = adam['t_joy']
# print(f"Adamning ismi {adam['ismi'].title()}, {t_yil}-yilda, {t_joy.title()} shahrida tug'ilgan.")
# oyim = {'ismi':'bayan', 't_yil':'1975', 't_joy':"qozog'iston", "malumot":"oliy", 'ish':'uy bekasi'}
# print(f"Oyimning ismi {oyim['ismi'].title()}, {oyim['t_yil']}-yilda, {oyim['t_joy'].title()} Respublikasida tug'ilgan, ma'lumoti {oyim['malumot']}, hozirda {oyim['ish']}")

# oila = {
#         'ali':'manti',
#         'vali':'kabob',
#         'hasan':'norin',
#         'husan':'dolma',
#         'olim':'qozonkabob'
#         }
# print(f"Alining sevimli taomi {oila['ali']}")

lugat = {
        'int':'butun son',
        'float':'haqiqiy son',
        'title':'bosh soz kattalashtiradi',
        'upper':'hammasini kattalashtiradi',
        'strip':'boshliqni olib tashlaydi',
        'append':'qoshadi',
        'get':'phone = telefonlar.get("hasan","Bunday ism mavjud emas")',
        'copitolize':'birinchi harfni katta qladi',
        'len':'uzunlikni aniqlaydi',
        'sort':'listni sortlaydi',
        'sorted':'list malumotlarini ozgartirmagan holda sortlaydi',
        'max':'maksimumini aniqlaydi',
        'list':'royhat',
        'tuple':'ozgarmas royhat',
        'remove':'qiymat qoshib ochirish',
        'lower':'harflarni hammasini kichiklashtiradi',
        'reverse':'boshini oxiriga, oxirini boshiga',
        'range':'juft_sonlar = list(range(0,20,2))',
        'insert':'listning istalgan joyiga element qoshish',
        'del':'ochirish',
        'pop':'elementni sugurib olish'
        }

soz = input("So'z kiriting: ").lower()
# if soz in lugat:
#     print(lugat[soz])
# else:
#     print("Bunday so'z mavjud emas!")
# print(lugat.get(soz, "Bunday so'z yo'q!"))

print(lugat[soz]) if soz in lugat else print("yoq")



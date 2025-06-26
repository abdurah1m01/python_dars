# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2020,
#         'narh':9000,
#         'km':89000,
#         'karobka':'mexanik'
# }

# car2 = {
#         'model':'gentra',
#         'rang':'mokriy',
#         'yil':2016,
#         'narh':20000,
#         'km':100000,
#         'karobka':'avtomat'
# }

# car = car0
# print(f"{car['model'].title()}, "\
#       f"{car['rang']} rangi, "\
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang, \
#   {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$") 


# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")


# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'nexia 3',
#         'rang':None,
#         'yil':2020,
#         'narh':None,
#         'km':0,
#         'karobka':'avto'
#     }
#     malibus.append(new_car)
#     for malibu in malibus[:3]:
#         malibu['rang']='qizil'
#     for malibu in malibus[3:6]:
#         malibu['rang']='qora'
#     for malibu in malibus[6:]:
#         malibu['rang']='mokri'
#         malibu['karobka']='mexanik'
#     for malibu in malibus:
#         if malibu['karobka']=='avto':
#             malibu['rarh']=40000
#         else:
#             malibu['narh']=35000

# print(malibus)

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','java'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'olim':['c++','c#']
# }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tilini biladi:", end='')
#     for til in tillar:
#         print(f' {til.upper()} ', end='')

# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']},
#     'vali':{'familiya':'shamsiyev',
#             'tyil':2001,
#             'malumot':'o\'rta',
#             'tillar':['php','sql']
#             },
#     'hasan':{'familiya':'hasanov',
#              'tyil':1999,
#              'malumot':'oliy',
#              'tillar':['html','css','java']}
# }
# for ism, info in hamkasblar.items():
#     print(f"{ism.title()} {info['familiya'].title()}, "\
#           f"{info['tyil']}-yilda tug'ilgan, "\
#           f"ma'lumoti {info['malumot']}. "\
#           f"Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())

# adabiyot0 = {
#     'ismi':'abu abdulloh muhammad',
#     'tyil':810,
#     'tjoy':'Buxoro',
#     'yasha':60,
#     'mashhur':['al-jome as-sahih','al-adab al-mufrad', 'at-tarix al-kabir', 'at-tarix as-sagir']
# }
# adabiyot1 = {
#     'ismi':'Abdulla qodiriy',
#     'tyil':1894,
#     'tjoy':'toshkent',
#     'yasha':44,
#     'mashhur':['o\'tkan kunlar', 'mehrobdan chayon', 'obid ketmon']
# }
# adabiyot2 = {
#     'ismi':'eRKIN vohidov',
#     'tyil':1936,
#     'tjoy':"fargona",
#     'yasha':80,
#     'mashhur':['tong nafasi', 'qo\'shiqlarim sizga', 'o\'zbegim', 'qiziquvchan matmusa']
# }
# adabiyot3 = {
#     'ismi':'alisher navoiy',
#     'tyil':1441,
#     'tjoy':'hirot',
#     'yasha':60,
#     'mashhur':['xamsa','lison ut-tayr', 'mahbub al-qulub']
# }
# adabiyotlar = [adabiyot0, adabiyot1, adabiyot2, adabiyot3]

# for ism in adabiyotlar:
#     print(f"{ism['ismi'].title()}, {ism['tyil']}-yilda {ism['tjoy']}da tug'ilgan, {ism['yasha']} yil umr ko'rgan")

# adabiyotlar = {
# 'adabiyot0' : {
#     'ismi':'abu abdulloh muhammad',
#     'tyil':810,
#     'tjoy':'Buxoro',
#     'yasha':60,
#     'mashhur':['al-jome as-sahih','al-adab al-mufrad', 'at-tarix al-kabir', 'at-tarix as-sagir']
# },
# 'adabiyot1' : {
#     'ismi':'Abdulla qodiriy',
#     'tyil':1894,
#     'tjoy':'toshkent',
#     'yasha':44,
#     'mashhur':['o\'tkan kunlar', 'mehrobdan chayon', 'obid ketmon']
# },
# 'adabiyot2' : {
#     'ismi':'eRKIN vohidov',
#     'tyil':1936,
#     'tjoy':"fargona",
#     'yasha':80,
#     'mashhur':['tong nafasi', 'qo\'shiqlarim sizga', 'o\'zbegim', 'qiziquvchan matmusa']
# },
# 'adabiyot3' : {
#     'ismi':'alisher navoiy',
#     'tyil':1441,
#     'tjoy':'hirot',
#     'yasha':60,
#     'mashhur':['xamsa','lison ut-tayr', 'mahbub al-qulub']
# }
# }
# for asar in adabiyotlar.values():
#     print(f"\n {asar['ismi'].title()}ning mashhur asarlari: ")
#     for til in asar['mashhur']:
#         print(til.upper())

# oilakino = {
#     'alish':['terminator', 'rambo', 'titanik'],
#     'vali':['tenet',"inseption", 'interestellar'],
#     'hadan':['abdullajon', 'bomba','shaytanat'],
#     'husan':['mahallada duv-duv gap', 'jon wick'],
#     'olim':['yura davri', 'terminator: genesis']
# }
# for kalit, qiymat in oilakino.items():
#     print(f"\n{kalit.title()}ning sevimli kinolari: ")
#     for til in qiymat:
#         if til == 'jon wick':
#             print(til.title())
#         else:
#             print(til.capitalize())

davlatlar = {
    'uzbekiston':{'poytaxt':'toshkent',
                   'hudud':448978,
                   'aholi':38000000,
                   'pulbir':'so\'m'},
    'russiya':{'poytaxt':'maskva',
                'hudud':17098246,
                'aholi':144000000,
                'pulbir':'rubl'
                },
    'aqsh':{'poytaxt':'vashington',
                   'hudud':9631418,
                   'aholi':327000000,
                   'pulbir':'dollar'},
    'malayziya':{'poytaxt':'kuala-lumpur',
                'hudud':329350,
                'aholi':25000000,
                'pulbir':'rinngit'
                },
}
# for davlat, qiymat in davlatlar.items():
#     if davlatlar == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {qiymat['poytaxt'].title()}"\
#           f"\nHududi: {qiymat['hudud']} kv.km"
#           f"\nAholsi: {qiymat['aholi']}"
#           f"\nPul birligi: {qiymat['pulbir']}")
    

nom = input("Davlat nomini kiriting: ").lower()
# if nom in davlatlar:
#     print(f"{davlatlar[nom].values()}")
# else:
#     print("Bizda bu davlat haqoida ma'lumot yo'q")
if nom in davlatlar:
    info = davlatlar[nom]
    if info == 'aqsh':
        print(f"\n{nom.upper()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['hudud']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pulbir']}")
    else:
        print(f"\n{nom.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['hudud']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pulbir']}")
else:
    print("Bizda bu davlat haqoida ma'lumot yo'q")

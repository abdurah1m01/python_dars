# def katta_harf(ismlar):   1
#     """"Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
#         harfini katta harfga o'zgatiruvchi funksiya"""
#     harflar = []
#     while ismlar:
#         ism = ismlar.pop()
#         harflar.append(ism.title())
#     return harflar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# harflar = katta_harf(talabalar[:])
# print(harflar)

# def katta_harf(matn):   2
#     for n in range(len(matn)):
#         matn[n]=matn[n].title()
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)


# def katta_harf(matn):
#     """"Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradi"""
#     for n in range(len(matn)):
#         matn[n]=matn[n].title()
#     return matn

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar[:])
# print(ismlar)
# print(yangi_ismlar)
talabalar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar = {}
    while ismlar:
        for ism in ismlar:
            baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
            baholar[ism]=baho
        return baholar

baholar = bahola(talabalar)
print(baholar)
print(talabalar)

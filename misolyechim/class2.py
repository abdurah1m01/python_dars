
class Avto:
    def __init__(self, model, rang, korobka, narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.km = 0
    
    def get_info(self):
        return f"Model: {self.model}, rang: {self.rang}, korobka: {self.korobka}, narxi: {self.narx}, km: {self.km}"
    
    def update_km(self):
        self.km += 1000
    
    def get_fullname(self):
        return f"{self.model} , {self.rang}"

class Avtosalon:
    def __init__(self, salon_nomi):
        self.sname = salon_nomi
        self.manzil = 'Yunusobod'
        self.sotuv = 0
        self.son = []

    def get_avto(self, avto):
        self.son.append(avto)
        self.sotuv += 1
    
    def get_avtos(self):
        return [x.get_fullname() for x in self.son]


avto1 = Avto('Versachi', 'oq', 'avtomat', 12000)
avto2 = Avto("Mers", 'qora', 'avtomat', 30000)
avto = Avtosalon('GM')
avto.get_avto(avto1)
avto1.update_km()
avto1.update_km()
print(avto1.get_info())
print(avto2.get_info())
print(avto3)

        



# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def set_bosqich(self, yangi_bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = yangi_bosqich

#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism

#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya

#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"

#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil


# class Fan:
#     """Fan nomli klass"""

#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi

#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [talaba.get_fullname() for talaba in self.talabalar]

#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni


# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith("__") is False]


# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Alimov", 2001)
# talaba3 = Talaba("Akrom", "Boriyev", 2001)
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)
# print(matematika.talabalar)
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# print(see_methods(Talaba))
# print(see_methods(talaba1))
# # print(see_methods(str))
# print(talaba1.__dict__)
# print(talaba1.__dict__.keys())

















# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

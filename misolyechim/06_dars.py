# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else: 
#         print(car.upper())

# ism = input("Login ismingizni kiriting: ")
# ismi = "ali"
# if ism != ismi:
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {ism}")

# login = input("Loginingiz: ")
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {login}")

# son1 = int(input("Son kiriting: "))
# son2 = int(input("2 sonni kiriting: "))
# if son1 == son2:
#     print("Sonlar teng")

# a = float(input("Istalgan son kiriting:"))
# # if a < 0:
# #     print("manfiy son")
# # else:
# #     print("musbat son")
# print("son manfiy") if a < 0 else print("musbat")

a = float(input("son kiriting: "))
# if a > 0:
#     print(a**(1/2))
# else:
#     print("musbat son kiriting!!!")
print(a**(1/2)) if a > 0 else print("Musbat son kirinting!!!")
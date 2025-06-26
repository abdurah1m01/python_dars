# kitob = ("Sevimli kitobingizni kiritning:")
# kitob += "(dasturni to'xtatish uchun 'stop' deb yozing!)"
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(kitob)
#     if qiymat != 'stop':
#         print(qiymat)

# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!')  

# savol = 'Yoshingizni kiriting: '
# savol += "(dastur tugatish uchun 'exit' yoki 'quit' deb yozing!)"
# # savol = int(savol)
# while True:
#     qiy = (input(savol))
#     if qiy == 'exit' or qiy == 'quit':
#         break
#     yosh = int(qiy)

#     if yosh<7:
#         print(f"7 yoshdagilarga 2000 so'm")
#     elif yosh<18:
#         print(f"7-18 yoshdagilarga 3000 so'm")
#     elif yosh<65:
#         print(f"18-65 yoshdagilarga 10000 so'm")
#     else:
#         print('tekin')
# print('Raxmat')     

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = float(input(savol))
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


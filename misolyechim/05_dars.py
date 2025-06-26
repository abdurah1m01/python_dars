# ismlar = ['Nodir', 'Kamol', 'Doniyor', 'Sarvar', 'Fozil']
# for s in ismlar:
#     print(s, 'salom')
# print(f"{len(s)} marta takrorlandi")

# sonlar = list(range(11, 100, 2))
# for kub in sonlar:
#     print(kub**3)
# kinolar = []
# print("5 ta eng yaqin do\'stingiz")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1} sevimli kinoingiz"))
# print(kinolar)

ismlar = []
a = int(input("Bugun nechta odam bilan gaplashdingiz? "))
for ism in range(a):
    ismlar.append(input(f"{ism+1}-suxbatdoshingiz kim: "))
print(ismlar)

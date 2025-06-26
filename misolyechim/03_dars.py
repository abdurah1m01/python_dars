# ismlar = ['G\'ulom', 'Sarvar', 'Hoshim']
# print('Nima gap ', ismlar[0])
# print(ismlar[1], " bugun futbolga borasanmi?")
# print("Workoutga borasanmi ", ismlar[2], 'bugun')

# sonlar = [134, 21, -42, 23.42, 123, -34.2, 21, -244]
# print(sonlar[0] + sonlar[3] - sonlar[-1])
# sonlar[4] = sonlar[4] + 432
# sonlar[5] = 344
# sonlar.append(343.34)
# sonlar.append(2453542)
# sonlar.insert(0, 76543)
# sonlar.insert(9, 87654)
# del sonlar[3]
# sonlar.remove(-244)
# sonlar.remove(21)
# print(sonlar)
# son = sonlar.pop(3)
# print(son)
# print(sonlar)

# t_shaxslar = ['Imom al-Buxoriy', 'Alisher Navoiy', 'Amir Temur','Cho\'lpon', 'Abdulla Avloniy', 'Maxmudxo\'ja Bexbudiy']
# z_shaxslar = ['Ilon Musk', 'Geytsbi', 'Bill Geyts', 'Abror Muxtorali', 'Toretto']
# t_shaxs = t_shaxslar.pop(0)
# z_shaxs = z_shaxslar.pop(3)
# print("Men taixiy shaxslardan", t_shaxs, 'bilan,\n', 'zamonaviy shaxslardan ', z_shaxs, 'bilan \n suxbat qilishni istar edim')
# print("Men taixiy shaxslardan", t_shaxslar[0], 'bilan,\n', 'zamonaviy shaxslardan ', z_shaxslar[0], 'bilan \n suxbat qilishni istar edim')

friends = []
friends.append("Begzot")
# print(friends)
friends.append("Diyor")
friends.append("Azim")
friends.append('Bunyod')
friends.append('Diyor')
friends.append('Muhammad')
# print(friends)
# friends.insert(0, 'Sarvar')
# print(friends)
# del friends[3]
# print(friends)
# friends.remove("Diyor")
# print(friends)
# friend = friends.pop(3)
# print(friends, friend)
friends.insert(0, "Sarvar")
friends.insert(3, 'Dilshod')
friends.insert(-1, 'Doniyor')
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-3))

print(mehmonlar)
#  n gacha bolgan dost sonlar

s =[]
a = int(input('son kiriting: '))
for i in range(1, a+1):
    for j in range(1, i+1):
        if i%j==0:
            s.append(i)
print(sum(s))
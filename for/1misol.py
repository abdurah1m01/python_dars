z = []
a = int(input('Son kiriting: '))
for i in range(1,a+1):
    if a%i==0:
        z.append(i)

print(z)
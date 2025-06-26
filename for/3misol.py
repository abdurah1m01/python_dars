a = int(input('butun son kiriting: '))
d=[]
for i in range(1,a):
    if a%i==0:
        d.append(i)
s = sum(d)
if s == a:
    print("mukammal")
else:
    print('mukammalmas')
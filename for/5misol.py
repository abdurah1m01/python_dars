a = int(input("butun son kiriting:"))
d=[]
for j in range(1, a):
       if j%3==0 and j%5!=0:
            d.append(j)
print(d)
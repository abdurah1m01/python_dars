
a=int(input("son kiriting: "))

f=[]
for i in range(1, a):
    g=0
    s=[]
    for j in range(1,i):
        if i%j == 0:
            s.append(j)
    g = sum(s)
    if i == g:
        f.append(i)
print(f)
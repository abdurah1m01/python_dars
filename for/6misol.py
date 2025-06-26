a = int(input('son kiriting: '))
w=[]
for i in range(a):
    w.append(False)
for i in range(2,a):
    if w[i] is True:
        continue    
    start=i+i      
    step=i
    for j in range(start, a,step):
            w[j]=True
    print("tub {}",step)

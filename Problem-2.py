import numpy as np

i = int(input("Enter Order:"))

Ar = np.ones((i,i))
diag_sum =0
for x in range(0,i):
    for y in range(0,i):
        print("Element %d%d" %(x,y))
        Ar[x,y] = int(input("Enter: "))
        if x == y:
            diag_sum += Ar[x,y]
s = 0
while s < i:
    diag_sum += Ar[i-1-s,s]
    s += 1
print(Ar)
Ar2 = np.ones((i-2,i-2))
to_sort = []
for x in range(0,i-2):
    for y in range(0,i-2):
        to_sort.append(Ar[x+1,y+1])
        
to_sort.sort()
z = 0
for x in range(0,i-2):
    for y in range(0,i-2):
       Ar2[x,y] = to_sort[z]
       z += 1
for x in range(0,i-2):
    for y in range(0,i-2):
        Ar[x+1,y+1]=Ar2[x,y]
print(Ar)
print("The sum of diagonal:" + str(diag_sum))

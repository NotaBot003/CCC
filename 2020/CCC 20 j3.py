n = int(input())

hix = 0
hiy = 0
lowx = 100
lowy = 100
for i in range(n):
    z = input().split(",")
    [x,y] = list(map(int, z))
    if x > hix:
        hix = x 
    if y > hiy:
        hiy = y 
        
    if x < lowx:
        lowx = x 
    if y < lowy:
        lowy = y
        
    #print (x,",",y)

        
hix = hix + 1
hiy = hiy + 1
lowx = lowx - 1
lowy = lowy - 1

#print (lowx, ",", lowy)
#print (hix, ",", hiy)
print(f"{lowx},{lowy}")
print(f"{hix},{hiy}")




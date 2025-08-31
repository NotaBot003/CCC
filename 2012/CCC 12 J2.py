f1 = int(input())
f2 = int(input())
f3 = int(input())
f4 = int(input())

if f1 > f2 > f3 > f4:
    print("Fish Diving")
elif f4 > f3 > f2 > f1:
    print("Fish Rising")
elif f1 == f2 == f3 == f4:
    print("Fish At Constant Depth")
else: print("No Fish")
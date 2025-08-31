useless = int(input())
string = input()

a = string.count("A")
b = string.count("B")

if a == b:
    print("Tie")
if a > b:
    print("A")
if a < b:
    print("B")
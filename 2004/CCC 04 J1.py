intt = int(input())
out = 0
square = 0
while square <= intt:
    out += 1
    square = out * out
print("The largest square has side length", str(out - 1) + ".")
adj = int(input())
noun = int(input())

out1 = []
out2 = []

for i in range(adj):
    out1.append(input())

for i in range(noun):
    out2.append(input())

for i in range(adj):
    for k in range(noun):
        print(out1[i] + " as " + out2[k])
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    rep = int(input())
    possible = True
    mt = []
    branch = [int(1e7)]
    required = 1
    for i in range(rep):
        mt.append(int(input()))
    pop = rep - 1
    while True:
        # print(branch[-1], mt[pop], required)
        if required > rep:
            break
        if pop >= 0:
            if mt[pop] == required:
                required += 1
                pop -= 1
            elif branch[-1] == required:
                branch.pop(-1)
                required += 1
            else:
                if mt[pop] > min(branch):
                    possible = False
                    # print('1')
                    break
                branch.append(mt[pop])
                pop -= 1
        else:
            if branch[-1] == required:
                branch.pop(-1)
                required += 1
            else:
                possible = False
                # print('2')
                break
    if possible:
        print('Y')
    else: print('N')

"""
40
13
14
12
15
11
16
17
18
19
20
10
21
8
9
22
23
24
25
6
7
26
27
28
29
4
2
3
5
30
31
32
33
34
35
36
37
38
39
1
40
"""

Debug = True
#Debug = False
if Debug: print('''ABCD
8
10
. . . . . A . . . .
. . D . . . B . D .
A B C D D . . C . .
. C . D C . D . D .
. D . C B . . C . A
. D C B A . D . B .
. . D . . . . C . A
. . D . . . D . . A
''')

W = input()
R = int(input())
C = int(input())
G = []
for i in range(R):
    row = list(input().split())

    G.append(row)
    if Debug: print(row)
if Debug: print(G)
def valid(r, c):
    if r < 0 or r > R - 1 or \
        c < 0 or c > C - 1:
        return False
    return True


cnt = 0
sz = len(W)
words = [W, W[::-1]]
if Debug: print(words)
for r in range(R):
    for c in range(C):
        for W in words:
            #Horizontal - L
            found = True
            for i in range(sz):
                if not valid(r, c + i):
                    found = False
                    break
                if G[r][c+i] != W[i]:
                    found = False
                    break
                if i ==0 or i == sz - 1:
                    continue
                #HL - up
                found_L = True
                for j in range(1, sz - i):
                    if not valid(r - j, c + i):
                        found_L = False
                        break
                    if G[r - j][c + i] != W[i + j]:
                        found_L = False
                        break
                if found_L:
                    cnt += 1
                    if Debug: print("HL - up")
                # HL - down
                found_L = True
                for j in range(1, sz - i):
                    if not valid(r + j, c + i):
                        found_L = False
                        break
                    if G[r + j][c + i] != W[i + j]:
                        found_L = False
                        break
                if found_L:
                    cnt += 1
                    if Debug: print("HL - down")
            if found:
                cnt += 1
                if Debug: print("H")
            #Horizontal - R
            found = True
            for i in range(sz):
                if not valid(r, c - i):
                    found = False
                    break
                if G[r][c - i] != W[i]:
                    found = False
                    break
                if i == 0 or i == sz - 1:
                    continue
                #HR - up
                found_L = True
                for j in range(1, sz - i):
                    if not valid(r - j, c - i):
                        found_L = False
                        break
                    if G[r - j][c - i] != W[i + j]:
                        found_L = False
                        break
                if found_L:
                    cnt += 1
                    if Debug: print("HR - up")
                # HR - down
                found_L = True
                for j in range(1, sz - i):
                    if not valid(r + j, c - i):
                        found_L = False
                        break
                    if G[r + j][c - i] != W[i + j]:
                        found_L = False
                        break
                if found_L:
                    cnt += 1
                    if Debug: print("HR - down")
            # if found:
            #   cnt += 1
            #   if Debug: print("H")
            # vertical
            found = True
            for i in range(sz):
                if not valid(r + i, c):
                    found = False
                    break
                if G[r+i][c] != W[i]:
                    found = False
                    break
            if found:
                cnt += 1
                if Debug: print("V")
            #Diagonal LT - RB
            found = True
            for i in range(sz):
                if not valid(r + i, c + i):
                    found = False
                    break
                if G[r + i][c + i] != W[i]:
                    found = False
                    break
                if not (i == 0 or i == sz - 1):
                    # LT - up
                    found_L = True
                    for j in range(1, sz - i):
                        if not valid(r + i - j, c + i + j):
                            found_L = False
                            break
                        if G[r + i - j][c + i + j] != W[i + j]:
                            found_L = False
                            break
                    if found_L:
                        cnt += 1
                        if Debug: print("LT -> RB L up")
                    # LT - down
                    found_L = True
                    for j in range(1, sz - i):
                        if not valid(r + j + i, c + i - j):
                            found_L = False
                            break
                        if G[r + j + i][c + i - j] != W[i + j]:
                            found_L = False
                            break
                    if found_L:
                        cnt += 1
                        if Debug: print("LT -> RB L down")
            if found:
                cnt += 1
                if Debug: print("LT -> RB")
            # Diagonal RB - RT
            found = True
            for i in range(sz):
                if not valid(r - i, c - i):
                    found = False
                    break
                if G[r - i][c - i] != W[i]:
                    found = False
                    break
                if not (i == 0 or i == sz - 1):
                    # LT - up
                    found_L = True
                    for j in range(1, sz - i):
                        if not valid(r - i - j, c - i + j):
                            found_L = False
                            break
                        if G[r - i - j][c - i + j] != W[i + j]:
                            found_L = False
                            break
                    if found_L:
                        cnt += 1
                        if Debug: print("RT - RB L up")
                    # LT - down
                    found_L = True
                    for j in range(1, sz - i):
                        if not valid(r - i + j, c - i - j):
                            found_L = False
                            break
                        if G[r - i + j][c - i - j] != W[i + j]:
                            found_L = False
                            break
                    if found_L:
                        cnt += 1
                        if Debug: print("RB -> LT L down")
            # if found:
            #     cnt += 1
            #     if Debug: print("LT -> RB")
            # Diagonal RT -  LB
            found = True
            for i in range(sz):
                if not valid(r + i, c - i):
                    found = False
                    break
                if G[r + i][c - i] != W[i]:
                    found = False
                    break
            if found:
                cnt += 1
                if Debug: print("RT ->  LB")


print(cnt)
"""
ABCD
8
10
. . . . . A . . . .
. . D . . . B . D .
A B C D D . . C . .
. C . D C . D . D .
. D . C B . . C . A
. D C B A . D . B .
. . D . . . . C . A
. . D . . . D . . A
18
"""
'''
RST
6
7
R S T X R S T
S X X X X X T
T X R S T X S
R X S X T X R
S X T X S X S
T X T S R S T
11
'''
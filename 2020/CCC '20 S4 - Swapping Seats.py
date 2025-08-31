import sys
input = sys.stdin.readline

def minswap(i, A, B, C, psa):
    # l, m, s = arr[i:i + len(a)].count(A), arr[i:i + len(a)].count(B), arr[i:i + len(a)].count(C)

    l, m, s = psa[A][i + len(a)] - psa[A][i], \
              psa[B][i + len(a)] - psa[B][i], \
              psa[C][i + len(a)] - psa[C][i], \

    # l_p, m_p, s_p = arr[i:l + i], arr[l + i:l + m + i], arr[l + m + i:len(a) + i]

    l_m, l_s = psa[B][l + i] - psa[B][i], \
               psa[C][l + i] - psa[C][i]
    m_l, m_s = psa[A][l + m + i] - psa[A][l + i], \
               psa[C][l + m + i] - psa[C][l + i]
    s_l, s_m = psa[A][len(a) + i] - psa[A][l + m + i], \
               psa[B][len(a) + i] - psa[B][l + m + i]

    # l_m, l_s = l_p.count(B), l_p.count(C)
    # m_l, m_s = m_p.count(A), m_p.count(C)
    # s_l, s_m = s_p.count(A), s_p.count(B)

    Ml = min(l_m, m_l)
    m_l -= Ml
    Mm = min(s_l, l_s)
    s_l -= Mm
    Ms = min(s_m, m_s)

    return (2 * m_l + 2 * s_l + Ms + Mm + Ml)

p = int(1e8)
a = input().strip()
arr = a * 2
psa = {'A':[0]*(len(arr)+1),
       'B':[0]*(len(arr)+1),
       'C':[0]*(len(arr)+1)}

for i in range(len(arr)):
    psa['A'][i+1] = psa['A'][i]
    psa['B'][i+1] = psa['B'][i]
    psa['C'][i+1] = psa['C'][i]
    ch = arr[i]
    psa[ch][i+1] += 1

print(psa)
for i in range(len(a)):
    p = min(p, minswap(i, 'A', 'B', 'C', psa))
    p = min(p, minswap(i, 'B', 'A', 'C', psa))
print(p)

"""
BABCBCACCA
"""


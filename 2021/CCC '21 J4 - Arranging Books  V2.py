arr = input()
l, m, s = arr.count("L"), arr.count("M"), arr.count("S")

l_p, m_p, s_p = arr[:l], arr[l:l+m], arr[l+m:]

l_m, l_s = l_p.count('M'), l_p.count('S')
m_l, m_s = m_p.count('L'), m_p.count('S')
s_l, s_m = s_p.count('L'), s_p.count('M')

Ml = min(l_m, m_l)
m_l -= Ml
Mm = min(s_l, l_s)
s_l -= Mm
Ms = min(s_m, m_s)

print(2 * m_l + 2 * s_l + Ms + Mm + Ml)

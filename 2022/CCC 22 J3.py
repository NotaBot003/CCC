s = input()
strings, digits, sign = "", "", ""
in_s, in_d = True, False
for i in range(len(s)):
    ch = s[i]
    if s[i].isalpha():
        if in_s:
            strings += ch
        else:
            #print("stings", strings)
            #print("digits", digits)
            if sign == "+":
                print(strings, "tighten", int(digits))
            else:
                print(strings, "loosen", int(digits))
            strings = ch
            digits = ""
            in_d = False
            in_s = True
    elif ch.isdigit():
        digits += ch
        in_s = False
    else: #sign
        sign = ch
if sign == "+":    print(strings, "tighten", int(digits))
else:              print(strings, "loosen", int(digits))

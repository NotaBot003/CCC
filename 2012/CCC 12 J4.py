import string

b = int(input())
word = input()


def out(char, a):
    new = ord(char) + 3 * (a + 1) + b
    new = 65 + (new - 91) if new > 90 else new
    return chr(new)


for i in range(len(word)):
    for output in string.ascii_uppercase:
        if out(output, i) == word[i]:
            print(output, end='')
            break
print()
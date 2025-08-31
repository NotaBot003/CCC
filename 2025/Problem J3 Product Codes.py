rep = int(input())

num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

for i in range(rep):
    total = 0
    temp = 'a' * 0
    numbers = []
    negative = False
    negatives = []
    time = 0
    code = input()
    final = "a" * 0
    for j in range(len(code)):
        if code[j] == '1' or code[j] == '2' or code[j] == '3' or code[j] == '4' or code[j] == '5' or code[j] == '6' or code[j] == '7' or code[j] == '8' or code[j] == '9' or code[j] == '0':
            if j != 0 and code[j-1] == "-":
                negative = True
            if j != 0 and (code[j - 1] == '1' or code[j - 1] == '2' or code[j - 1] == '3' or code[j - 1] == '4' or code[j - 1] == '5' or code[j - 1] == '6' or code[j - 1] == '7' or code[j - 1] == '8' or code[j - 1] == '9' or code[j - 1] == '0'):
                temp += code[j]
            else:
                if negative:
                    negatives.append(time)
                    numbers.append(temp)
                    negative = False
                    time += 1
                else:
                    numbers.append(temp)
                    negative = False
                    time += 1
                temp = code[j]
    del numbers[0]
    numbers.append(temp)
    for i in range(len(negatives)):
        numbers[negatives[i]] = '-' + numbers[negatives[i]]
    for i in range(len(numbers)):
        total += int(numbers[i])
    for i in range(len(code)):
        if 64 < ord(code[i]) < 96:
            final += code[i]
    print(final + str(total))

'''
1
PL12N-2G1234Duytrty8-86tyaYySsDdEe
'''
n = int(input())
response = []
correct = []
time = 0
output = 0
for i in range(n):
    input1 = input()
    response.append(input1)
# print(response)
for i in range(n):
    input2 = input()
    correct.append(input2)
# print(correct)
for i in range(n):
    if response[time] == correct[time]:
        output += 1
    time += 1
print(output)

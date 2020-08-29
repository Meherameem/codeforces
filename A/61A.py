first = input()
second = input()
str = ''
for i in range(len(first)):
    if first[i] == second[i]:
        str = str + '0'
    else:
        str = str + '1'
print(str)
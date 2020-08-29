n = input().split('+')
n = sorted(n)
s = ''
temp = 0
for i in n:
    if temp == 0:
        s = s + i
    elif temp != 0:
        s = s + '+' + i
    temp = temp + 1
print(s)
x = 0
n = input()
n = int(n)
i = 0
l = list()
while (i < n):
    p = input()
    l.append(p)
    i = i + 1
for j in l:
    if j == 'X++' or j == '++X':
        x = x + 1
    elif j == 'X--' or j == '--X':
        x = x - 1
print(x)
n = input()
s = input()
l = list()
c = 0
for i in s:
    l.append(i)
for j in range(len(l) - 1):
    if l[j] == l[j + 1]:
        c = c + 1
    j = j + 1
print(c)

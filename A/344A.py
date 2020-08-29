s = input()
l = list()
count = 1
for i in range(int(s)):
    x = input()
    l.append(x)
for i in range(len(l) - 1):
    if l[i] == l[i + 1]:
        count = count
    else:
        count = count + 1
print(count)

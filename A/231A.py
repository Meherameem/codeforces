n = input()
n = int(n)
i = 0
s = list()
m = 0

c = 0
while (i < n):
    x = input()
    s.append(x)
    i = i + 1
for i in s:
    c1 = 0
    x, y, z = i.split()
    x = int(x)
    y = int(y)
    z = int(z)
    if x != m:
        c1 = c1 + 1
    if y != m:
        c1 = c1 + 1
    if z != m:
        c1 = c1 + 1
    if c1 >= 2:
        c = c + 1
print(c)
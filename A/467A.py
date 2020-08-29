n = int(input())
c = 0
i = 0
while (i < n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    z = y - x
    if z >= 2:
        c = c + 1
    i = i + 1
print(c)
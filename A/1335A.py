n = int(input())
l = []
for i in range(n):
    s = int(input())
    l.append(s)
for i in l:
    if i % 2 == 0:
        x = int(i / 2) - 1
        print(x)
    else:
        x = int(i / 2)
        print(x)
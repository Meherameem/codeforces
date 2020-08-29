n = int(input())

i = 0
l1 = list()
l2 = list()
l3 = list()
while (i < n):
    x, y, z = input().split()
    l1.append(int(x))
    l2.append(int(y))
    l3.append(int(z))

    i = i + 1

if sum(l1) == 0 and sum(l2) == 0 and sum(l3) == 0:
    print('YES')
else:
    print('NO')
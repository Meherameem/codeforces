s, n = map(int, input().split())
l1 = []
l2 = []
for i in range(n):
    inp = input()
    l = inp.split()
    for i in l:
        l1.append(int(i))
    l2.append(l1)
    l1 = []
l2.sort()
for i in range(len(l2) - 1):
    x = l2[i]
    y = l2[i + 1]
    z = []
    if x[0] == y[0]:
        if x[1] < y[1]:
            z = x
            l2[i] = y
            l2[i + 1] = z
count = n
for m in l2:
    if s <= m[0]:
        print('NO')
        break
    else:
        s = s + m[1]
        count = count - 1
if count == 0:
    print('YES')
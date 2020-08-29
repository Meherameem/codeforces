n = int(input())
s = input()
l = s.split()
l2 = []
lo = []
lt = []
lth = []
for i in l:
    l2.append(int(i))
one = l2.count(1)
two = l2.count(2)
three = l2.count(3)
if one == 0 or two == 0 or three == 0:
    print(0)
else:
    l3 = [one, two, three]
    count = min(l3)
    i = 0
    for i in range(len(l2)):
        if l2[i] == 1:
            lo.append(i + 1)
        elif l2[i] == 2:
            lt.append(i + 1)
        elif l2[i] == 3:
            lth.append(i + 1)

    print(count)

    for p in range(count):
        print(lo[p], lt[p], lth[p])
s = input()
p = input()
p = p.split()
l = list()
l2 = list()
count = 0
for i in p:
    l.append(int(i))
for j in range(len(l) - 1):
    m = l[j]
    n = l[j + 1]
    if m <= n:
        count = count + 1


    else:

        k = count + 1
        l2.append(k)
        count = 0

h = count + 1
l2.append(h)

print(max(l2))
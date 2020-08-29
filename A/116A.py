n = input()
n = int(n)
i = 0
l1 = list()
l2 = list()
l3 = list()
c = 0
while (i < n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    l1.append(a)
    l2.append(b)
    i = i + 1
for j in range(len(l1)):
    c = c + l2[j] - l1[j]
    l3.append(c)
print(max(l3))
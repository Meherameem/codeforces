n = int(input())
s = input()
l2 = list()
lb = list()
ls = list()
bigx = 0
smallx = 0
l = s.split()
for i in l:
    l2.append(int(i))
big = max(l2)
small = min(l2)
for i in range(len(l2)):
    if l2[i] == big:
        lb.append(i)
        if len(lb) > 1:
            bigx = min(lb)
        elif len(lb) == 1:
            bigx = lb[0]

for i in range(len(l2)):
    if l2[i] == small:
        ls.append(i)
        if len(ls) > 1:
            smallx = max(ls)
        elif len(ls) == 1:
            smallx = ls[0]
count = 0
if smallx < bigx:
    count = (bigx - 0) + (n - 1 - smallx) - 1

if smallx > bigx:
    count = (bigx - 0) + (n - 1 - smallx)

print(count)
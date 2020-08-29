n = int(input())
s = input().split()
l = []
count = 0
for i in s:
    l.append(int(i))
l2 = []
big = l[0]
small = l[0]
flag = True
for j in l:
    if j > big:
        big = j
        count = count + 1
    elif j < small:
        small = j
        count = count + 1

print(count)
import math

n, h = map(int, input().split())
s = input()
l = list(s.split(" "))
count = 0
for i in l:
    if int(i) <= h:
        count = count + 1

    else:
        x = math.ceil(int(i) / h)
        count = count + x

print(count)

x, y, z = map(int, input().split())
l = [x, y, z]
big = max(l)
small = min(l)
dis = 0
for i in l:
    if i != big and i != small:
        dis = dis + (big - i) + (i - small)
print(dis)
a, b, c, d = map(int, input().split())
li = [a, b, c, d]
li.sort()
a = li[3] - li[0]
b = li[3] - li[1]
c = li[3] - li[2]
print(a, b, c)
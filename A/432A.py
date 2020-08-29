n, k = map(int, input().split())
s = input()
l = s.split()
l2 = []
for i in l:
    if 5 - int(i) >= k:
        l2.append(int(i))
x = int((len(l2)) / 3)
print(x)
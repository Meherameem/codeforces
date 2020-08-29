k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)
i = 0
s = 0
while (i < w):
    i = i + 1
    c = i * k
    s = s + c
if s > n:
    print(s - n)
else:
    print(0)
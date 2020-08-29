n = int(input())
l = []
for i in range(n):
    s = input().split()
    l.append(s)
m = 0
c = 0
for i in l:
    if i[0] > i[1]:
        m = m + 1
    elif i[0] < i[1]:
        c = c + 1
if m > c:
    print('Mishka')
elif m < c:
    print('Chris')
elif m == c:
    print('Friendship is magic!^^')
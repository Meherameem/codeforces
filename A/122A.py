n = int(input())
a = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
c = 0
for i in a:
    r = n % i
    if r == 0:
        c = c + 1
if c != 0:
    print('YES')
else:
    print('NO')
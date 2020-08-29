n, k = map(int, input().split())
i = 1
count = 1
m = n
while i > 0:
    if (n % 10) == 0:
        print(count)
        break
    elif k == (n % 10):
        print(count)
        break
    else:
        count = count + 1
        n = count * m
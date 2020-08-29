n, m = map(int, input().split())
if n == m:
    print(str(n) + ' ' + '0')
elif n > m:
    dif = n - m
    rest = int(dif / 2)
    print(str(m) + ' ' + str(rest))
elif n < m:
    dif = m - n
    rest = int(dif / 2)
    print(str(n) + ' ' + str(rest))
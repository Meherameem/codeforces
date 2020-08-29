import math

n, k = map(int, input().split())
if k <= (math.ceil(n / 2)):
    x = 2 * (k - 1) + 1
    print(x)
else:
    x = 2 * (k - math.ceil(n / 2))
    print(x)
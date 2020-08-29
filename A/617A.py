import math

n = input()
n = int(n)
i = 5
c = 0
while (i > 0):
    a = n / i

    c = c + math.floor(a)

    b = n % i

    if b == 0:
        break
    else:
        n = b
    i = i - 1

print(int(c))

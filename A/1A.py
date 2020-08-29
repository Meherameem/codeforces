s = input()
n, m, a = s.split()
n = int(n)
m = int(m)
a = int(a)
x = int(n / a)

if (n % a) != 0:
    x = x + 1
y = int(m / a)

if (m % a) != 0:
    y = y + 1
print(x * y)
a = int(input())
b = int(input())
c = int(input())
sum = a + b + c
mul = a * b * c
p = (a + b) * c
r = a * (b + c)
s = (a * b) + c
u = a + (b * c)

print(max(sum, mul, p, r, s, u))
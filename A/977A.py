n, k = input().split()
count = 0
sum = 0
for i in range(int(k)):
    if n[-1] == '0':
        n = n[:-1]
    else:
        n = str(int(n) - 1)
print(n)
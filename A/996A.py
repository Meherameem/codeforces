n = int(input())
note = [100, 20, 10, 5, 1]
count = 0
for i in note:
    count = count + int(n / i)
    n = n % i
print(count)
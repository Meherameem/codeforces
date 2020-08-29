n, k = map(int, input().split())
count = 0
x = 0
r = 0
left_time = 240 - k
for i in range(n):
    x = x + 5 * (i + 1)
    if x <= left_time:
        count = count + 1
print(count)
n, m = map(int, input().split(' '))
tiles_no = list(map(int, input().split(' ')))
tiles_no.sort()
min_diff = list()
for i in range(m - n + 1):
    sub = tiles_no[n + i - 1] - tiles_no[i]
    min_diff.append(sub)
print(min(min_diff))
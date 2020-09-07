n, t = map(int, input().split())
s = input()
c = 0
while t > 0:
    if 'BG' in s:
        s = s.replace('BG', 'GB')
        t = t - 1
    else:
        break

print(s)
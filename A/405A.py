n = input()
s = list(map(int, input().split()))
s = sorted(s)
l = ''
for i in s:
    l = l + ' ' + str(i)
print(l.rstrip().lstrip())
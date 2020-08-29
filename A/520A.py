n = int(input())
s = input()
l = list()
count = 0
s = s.lower()
if len(s) < 26:
    print('NO')
else:
    s = set(s)
    if (len(s)) != 26:
        print('NO')
    else:
        print('YES')

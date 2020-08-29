n = int(input())
final = list()
x = input()
y = input()
final = final + (x[2:].split(' ')) + (y[2:].split(' '))
final = list(dict.fromkeys(final))
i = 1
count = 0
while i <= n:
    if str(i) in final:
        count = count + 1
        i = i + 1
    else:
        i = i + 1
        continue
if count == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')

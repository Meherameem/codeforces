n = input()
s = input()
l = list()
n = s.split()
for i in n:
    if i == ' ':
        continue
    else:
        l.append(int(i))
l.sort(reverse=True)
if len(l) == 1:
    print(1)
else:
    for i in range(len(l) - 1):
        sum1 = 0
        sum2 = 0
        sum1 = sum1 + sum(l[:i + 1])
        sum2 = sum2 + sum(l[i + 1:])
        if sum1 > sum2:
            k = i + 1
            print(k)
            break
        elif sum1 == sum2:
            m = i + 2
            print(m)
            break

        else:
i = 1
injured = list()
while i <= 4:
    x = input()
    injured.append(x)
    i = i + 1
total = int(input())
i = 1
all = list()
if '1' in injured:
    print(total)
else:
    while i <= total:
        for j in injured:
            if i % int(j) == 0:
                all.append(i)
            else:
                continue
        i = i + 1
    all = list(dict.fromkeys(all))
    print(len(all))

no = input()
lst = list()
n = int(no)
while n != 0:
    s = input()
    lst.append(s)
    n = n - 1

for item in lst:
    list(item)
    if len(item) <= 10:
        print(item)
    else:
        x = item[0]
        y = item[-1]
        p = x + str(len(item) - 2) + y
        print(p)
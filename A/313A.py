n = int(input())
if n >= 0:
    print(n)
else:
    x = str(n)
    if len(x) > 2:
        if len(x) == 3:
            if '0' in x:
                print(0)
            else:
                if x[(len(x)) - 1] >= x[len(x) - 2]:
                    print(x[:-1])
                else:
                    print((x[:-2]) + (x[len(x) - 1]))
        else:
            if x[(len(x)) - 1] >= x[len(x) - 2]:
                print(x[:-1])
            else:
                print((x[:-2]) + (x[len(x) - 1]))
    else:
        print(0)
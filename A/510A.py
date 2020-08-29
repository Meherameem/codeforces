n, m = map(int, input().split())
i = 0
j = 1
for i in range(n):
    # print('i=',i,'j=',j)
    if i % 2 == 0:
        print(m * '#')
    else:
        if i == j:
            print((m - 1) * '.' + '#')
            j = j + 4

        else:
            print('#' + (m - 1) * '.')
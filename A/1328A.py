n = int(input())
l2 = []
l3 = []
for i in range(n):
    s = input()
    l = s.split()
    for j in l:
        l2.append(int(j))
    l3.append(l2)
    l2 = []
for i in l3:
    left = i[0] % i[1]
    if left == 0:
        print(0)
    else:
        need = i[1] - left
        print(need)
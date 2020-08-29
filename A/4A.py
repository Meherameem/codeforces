s = input()
s = int(s)
if s <= 2:
    print("NO")
elif s <= 100:
    if (s % 2) == 0:
        print("YES")
    else:
        print("NO")
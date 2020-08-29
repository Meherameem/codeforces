s = input()
a = s.isupper()
b = s[0].islower()
c = s[1:].isupper()
if a == True:
    p = ''
    p = p + s.lower()
    print(p)

elif b == True:
    if len(s) == 1:
        print(s.upper())
    else:
        if c == True:
            p = ''
            p = p + s[0].upper() + s[1:].lower()
            print(p)

        else:
            print(s)

else:
    print(s)





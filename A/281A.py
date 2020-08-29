x = input()
s = list()
for i in x:
    s.append(i)
s[0] = s[0].upper()
print(''.join(s))
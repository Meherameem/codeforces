s = input()
s = s[1:-1]
count = 0
l = list()
s = s.replace(" ", "")
s = s.replace(",", "")
for i in s:

    if i not in l:
        count = count + 1
        l.append(i)
print(count)
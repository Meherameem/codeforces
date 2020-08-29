s = input()
countlow = 0
countup = 0
for i in s:
    if (i.islower()):
        countlow = countlow + 1
    elif (i.isupper()):
        countup = countup + 1
if countup > countlow:
    print(s.upper())
else:
    print(s.lower())
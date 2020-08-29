n = int(input())
s = input()
l = s.split()
x = 0
for i in l:
    if i == '1':
        print('HARD')
        break
    else:
        x = x + 1
if x == n:
    print('EASY')
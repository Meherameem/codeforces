x, y = map(int, input().split(' '))
years = 0
n = 0
limak = x
bob = y
while n == 0:
    years = years + 1
    limak = years * 3 * limak
    bob = years * 2 * bob
    if limak > bob:
        print(years)
        break
    else:
        n == 0

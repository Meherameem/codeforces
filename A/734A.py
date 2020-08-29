games_no = input()
string = input()
countA = string.count('A')
countD = string.count('D')
if countA > countD:
    print('Anton')
elif countA < countD:
    print('Danik')
else:
    print('Friendship')
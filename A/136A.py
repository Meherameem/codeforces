n = input()
output = [0] * int(n)
pi_no_friend = list(map(int, input().split(' ')))
for i in range(len(pi_no_friend)):
    x = i + 1
    y = pi_no_friend[i] - 1
    output[y] = x
print(' '.join(map(str, output)))
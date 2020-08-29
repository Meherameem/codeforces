n = int(input())
s = input().split()
numbers = list(map(int,s))

even = []
odd = []
for i in numbers:
    if (i%2) == 0:
        even.append(i)
    elif (i%2) != 0:
        odd.append(i)
if len(even) == 1 :
    index = numbers.index(even[0]) + 1
else:
    index = numbers.index(odd[0]) + 1
print(index)

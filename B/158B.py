import math
n = int(input())
group = input().split()
groups=[]
for i in group:
    groups.append(int(i))
ones=groups.count(1)
twos=groups.count(2)
threes=groups.count(3)
fours=groups.count(4)
cars = 0
cars += fours
cars += threes
cars += twos / 2
ones -= threes
if twos % 2 != 0:
    cars += 1
    ones -= 2
if ones > 0:
    cars += int(ones / 4)
    if ones % 4 != 0:
        cars += 1
print(str(int(cars)))
 
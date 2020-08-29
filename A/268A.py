n=int(input())
l=list()
l1=list()
l2=list()
l3=list()
i=0
while i< n:
    i = i + 1
    s=input()
    l=s.split()
    l1.append(l)
for i in l1:
    l2.append(i[0])
    l3.append(i[1])
count=0
for k in l2:
    for l in l3:
        if k==l:
            count=count+1
print(count)
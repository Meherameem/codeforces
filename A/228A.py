s=input()
l=s.split()
li=list()
count=0
for i in l:
    if i in li:
        count=count+1
        li.append(i)
    else:
        li.append(i)
print(count)
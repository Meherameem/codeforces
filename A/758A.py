n=int(input())
s=input().split()
l=[]
count=0
for i in s:
    l.append(int(i))
big=max(l)
for j in l:
    count=count+(big-j)
print(count)
i=0
s=list()
t=list()
r=0
while(i<5):
    n=input()
    s.append(n)
    i=i+1
for f in s:
    t=f.split( )
    r=r+1
    c=0
    for q in t:
        c=c+1
        q = int(q)
        if q == 1:
            a=3-r
            b=3-c
            a=abs(a)
            b=abs(b)
            print(a+b)
    n=int(input())
    s=input()
    li=s.split()
    l=list()
    for i in li:
        i=int(i)
        l.append(i)
    sum=sum(l)
    p=(sum/(n*100))*100
    print(p)
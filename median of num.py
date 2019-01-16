n=int(raw_input())
l=raw_input().split()
l=[int(i) for i in l]
l.sort()
if len(l)==n:
    if len(l)%2==0:
        x=len(l)/2
        print float(l[x]+l[x-1])/2
    else:
        y=len(l)/2
        print l[y]
else:
    print"invalid"

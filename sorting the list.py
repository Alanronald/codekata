n=int(raw_input())
l=raw_input().split()
l=[int(i) for i in l]
if len(l)==n:
    l.sort()
    print l
else:
    print"invalid"

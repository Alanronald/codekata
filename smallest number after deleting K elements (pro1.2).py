from itertools import combinations
i,n1=map(int,raw_input().split())
n2=len(str(i))
a=list(combinations(str(i),n2-n1))
a=(sorted(a))
b="".join(a[0])
print(b)

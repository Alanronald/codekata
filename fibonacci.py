n=int(input())
a=0
b=1
print b,
while(n-1):
    c=a+b
    a=b
    b=c
    print c,
    n=n-1

a=raw_input().split()
x=int(a[0])
y=int(a[1])
x = x ^ y; 
y = x ^ y;
x = x ^ y;
print x," ",y

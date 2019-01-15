a,b=raw_input().split()
a=int(a)
b=int(b)
for i in range(a+1,b):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print i

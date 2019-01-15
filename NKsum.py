n,k=raw_input().split()
n=int(n)
k=int(k)
list=raw_input()
list=list.split()
if len(list)==5:
    sum = 0
    for i in range(0,k):
        sum+=int(list[i])
    print(sum)
else:
    print"invalid"

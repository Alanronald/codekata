n=int(input())
a=[]
for k in range(0,n):  
    d=input()
    a.append(d)
list=[]
for k in zip(*a):
    if (k.count(k[0])==len(k)): 
        list.append(k[0])
    else:
        break
print(''.join(list))

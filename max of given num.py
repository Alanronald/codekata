a=int(raw_input())
list=raw_input().split()
list=[int(i) for i in list]
if len(list)==a:
    print max(list)
else:
    print"invalid"

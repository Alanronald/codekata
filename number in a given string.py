inp=raw_input()
a=[]
for c in inp:
    if c.isdigit():
        a.append(c)
print len(a)

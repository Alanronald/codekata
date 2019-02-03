inp=raw_input()
a=[]
for c in inp:
    if c.isdigit() or c.isalpha():
        continue
    else:
        a.append(c)
print len(a)

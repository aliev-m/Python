s=sorted([int(i) for i in input().split()])
x=[]
for i in s:
    if (s.count(i) > 1 ) and (x.count(i) == 0):
        x.append(i)
print (*x, sep=' ')
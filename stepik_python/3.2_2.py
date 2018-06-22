d=dict()
s=[i for i in input().lower().split()]
for i in s:
    d[i]=s.count(i)
for j in d:
    print(j+' '+str(d[j]),end=' ')

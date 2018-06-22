s=[int(i) for i in input().split()]
x=int(input())
indexi=[]
j=0
#for i in range(0,j):
for j in s:
    if j == x:
        indexi.append(s.index(j))
        s[s.index(j)]=x+1
if len(indexi) > 0:
    print(*indexi,sep=' ')
else:
    print('Отсутствует')
n=int(input())
i=1
j=0
s=[]
result=''
while i <= n:
    for j in range(1, i+1):
        s.append(i)
    i+=1
print (*s[0:n],sep=' ')
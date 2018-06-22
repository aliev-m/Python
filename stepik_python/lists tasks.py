s=[int(i) for i in input().split()]
i=0
j=len(s)-1
if len(s) == 1:
    print(s[0])
else:
    while i < (len(s)):
        if i == 0:
            print(s[i+1]+s[j],end=' ')
            i+=1
        elif i == j:
            print(s[i-1]+s[0],end=' ')
            i+=1
        else:
            print(s[i-1]+s[i+1],end=' ')
            i+=1










#j=0
#x=0
#while j<(len(s)):
#    x+=int(s[j])
#    j+=1
#print(x)




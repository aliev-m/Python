#s=input().upper()
#print((s.count('G')+s.count('C'))/len(s)*100)

#
#s = 'abcdefghijk'
#print(s[3:6])
#print(s[:-6])

#s=input()
s='aaaabbbbbccccaaaaa'
i=0
j=len(s)-1
result=s[i]
count=1
while i < j:
    if s[i] == s[i+1]:
        count+=1
        print(count)
        i+=1
    else:
        result+=str(count)
        result+=s[i+1]
        i+=1
        count=1
result+=str(count)
print(result)

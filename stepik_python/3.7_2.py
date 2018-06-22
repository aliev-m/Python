s1=input()
s2=input()
s3=input()
s4=str(input())
S=dict(zip(s1,s2))
for i in s3:
    print(str(S[i]),end='')
S2=dict(zip(s2,s1))
for j in s4:
    print(str(S2[j]),end='')



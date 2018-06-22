s=[]
N=0
M=0
result=[]
#for x in range(3):
while True:
    lst=input()
    if lst == 'end':
        break
    else:
        s.append([int(i) for i in lst.split()])
        N+=1
M=len(s[0])

result=[[0 for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        #if i == N-1:
        #    result[i][j] = (s[i - 1][j]) + (s[i- N + 1][j]) + (s[i][j - 1]) + (s[i][j + 1])
        #elif j == M-1:
        #    result[i][j] = (s[i - 1][j]) + (s[i + 1][j]) + (s[i][j - 1]) + (s[i][j - M + 1])
        #elif (j == M-1) and (i == N-1):
        #    result[i][j] = (s[i - 1][j]) + (s[i - N + 1][j]) + (s[i][j - 1]) + (s[i][j - M + 1])
       # else:
            result[i][j]=(s[i-1][j])+(s[(i+1)%N][j])+(s[i][j-1])+(s[i][(j+1)%M])

for i in range(N):
#print(s)
#print(result)
    print(' '.join(map(str,result[i])))
#print(N, M)
s=sorted([int(i) for i in input().split()])
i=0
if len(s) > 1:
    if (s[0] + s[1] == 0):
        print(s[0], end=' ')
    while i < len(s)-1:
        if (s[i] == s[i+1]) and (s[i] != s[i-1]) and (s[i] !=0):
                print(s[i],end=' ')
        i += 1
sum=0
sum2=0
while True:
    s=int(input())

    if (sum + s) == 0:
        print ((sum2)+(s**2))
        break
    else:
        sum+=s
        sum2+=s**2
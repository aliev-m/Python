result=''
mnoj=''
sum=''
with open('C:\dataset_3363_2.txt') as inf:
    s=inf.readline().strip()
s+='X'
for i in range(len(s)-1):
    if s[i].isalpha():
        if  s[i+2].isdigit():
            sum += str(s[i+1])
            sum += str(s[i + 2])
            result+=s[i]*int(sum)
            sum=''
        else:
            sum+=str(s[i+1])
            result += s[i] * int(sum)
            sum = ''
with open('C:\win.txt', 'w') as ouf:
    ouf.write(result)
print(result)


text = open("c:\dataset_3363_3.txt", 'r')
s = sorted(text.read().replace('\n', ' ').lower().split())
text.close()
counter=0
for i in s:
    if s.count(i)>counter:
        counter=s.count(i)
        result=i
print(result,counter,end='')
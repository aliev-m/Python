import requests
ur='https://stepic.org/media/attachments/course67/3.6.3/'
r='699991.txt'
url=ur+r
while r.find('We') == -1:
    url=ur+r
    r=requests.get(url.strip()).text
    print(r)
    '''
j=0
for i in r.text.splitlines():
    j+=1
print(j)
'''
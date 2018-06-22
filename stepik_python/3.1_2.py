l=[0,8]
def modify_list(l):
    j=len(l)-1
    for i in range(len(l)):
        if l[j]%2 == 0:
            l[j]=l[j]//2

        else:
            l.remove(l[j])
        j-=1
    return l
print(modify_list(l))
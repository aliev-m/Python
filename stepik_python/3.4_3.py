i, sa, s1, s2, s3, lc = 0, 0, 0, 0, 0, 0

with open('c:\dataset_3363_4.txt', 'r') as inp:
    for line in inp:
        line=line.strip()
        line=line.split(';')

        for i in range(1,4):
            sa+=float(line[i])/3
        print(sa)
        sa=0
        s1 += float(line[1])
        s2 += float(line[2])
        s3 += float(line[3])
        lc+=1
print(s1/lc, s2/lc, s3/lc, end=' ')

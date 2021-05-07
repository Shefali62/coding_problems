l=[]
for i in range(int(input())):
    a,c,d,p,q,r,j=input(),0,0,0,0,0,0
    for j in a:
        if j=='@':
            p=1
            continue
        if j=='.':
            break
        if p==0:
            d+=1
            if j.isdigit() or j.isalpha() or j=='-' or j=='_':
                c+=1
        if p==1:
            r+=1
            if j.isdigit() or j.isalpha():
                q+=1
    if d==c and r==q and a[len(a)-1:len(a)-5:-1]=='moc.':
        l.append(a)
l.sort()
print(l)

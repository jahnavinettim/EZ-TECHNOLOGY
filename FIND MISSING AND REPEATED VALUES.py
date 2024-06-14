FIND MISSING AND REPEATED VALUES

r=3
c=3
a=[]
for i in range(0,r):
    sub=[]
    print("enter values for row")
    for j in range(0,3):
        print("enter values for column")
        ele=int(input())
        sub.append(ele)
        print(sub)
        a.append(sub) 
        print(a)
d={}
ans={}
for i in range(0,r):
     for j in range(0,c):
         if a[i][j] not in d:
             d[a[i][j]]=1
         else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                a.append(a[i][j])
print(d)
for i in range(1,r**2+1):
    if i not in d:
        a.append(i)
print(d)
print(ans)

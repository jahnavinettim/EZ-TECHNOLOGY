s=input().split()
s=s[::-1]
print(*s,sep=" ")


s=input()
print(s)
l=list(s)
i=0
j=len(l)-1
while i<=j:
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    i+=1
    j-=1
print(''.join(l))
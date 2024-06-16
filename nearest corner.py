s=list(input().split())
chair=input()
z=999
c_ind =s.index(chair)
for i in range(0,c_ind):
    if s[i]=="-":
        if abs(c_ind-1)-1<z:
                ans=abs(i-c_ind)-1
for i in range(c_ind+1,len(s)):
    if s[i]=="-":
        if abs(i-c_ind)-1<z:
                z=abs(i-c_ind)-1
print(z)
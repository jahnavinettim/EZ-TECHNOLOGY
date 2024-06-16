a=[1,2,3]
b=[3,4,5]
mini=999
for i in range(len(a)):
    if a[i]+b[i]<mini:
        mini=a[i]+b[i]
print(mini)

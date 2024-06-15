s=input()
v="aeiou"
d={}
for i in s:
    if i in v:
        if i not in d:
            d[i]=1
        else:
            d[i] +=1
print(d)
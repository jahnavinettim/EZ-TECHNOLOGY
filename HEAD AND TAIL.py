s=input()
hc=0
tc=0
score=0
for i in s:
    if i=="H" or i=="h":
        tc=0
        hc+=1
        score+=2
        if hc==3:
            break
        else:
            hc=0
            tc +=1
            score -=1
            if tc==3:
                break
print(score)

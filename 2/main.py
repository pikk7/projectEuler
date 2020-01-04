fibonacchi=[1,2]
rtm=0
summa=2
i=2
while(rtm<4000000):
    
    fibonacchi.append(fibonacchi[i-1]+fibonacchi[i-2])
    print(fibonacchi[i])
    rtm=fibonacchi[i]
    #print(rtm)
    if(rtm%2==0):
        summa=summa+rtm
    i=i+1
print(summa)

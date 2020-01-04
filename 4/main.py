def isPalidrom(n):
    n=str(n)
    i=0
    j=len(n)-1
    while(i<len(n)/2):
        
        if(n[i]!=n[j]):
            return False
        i=i+1
        j=j-1
    return True


i=999
j=999
palidroms=[]
sajt=True
while(j>99):
    while(i>99):
        rtm=j*i
        #print(rtm)
        if(isPalidrom(rtm)):
            #print(str(j)+" "+str(i))
            print("----------------------")
            print(rtm)
            palidroms.append(rtm)
        i=i-1
    i=999
    j=j-1
    
        

        
print(max(palidroms))

import math

dividers=[]
def euler_tetel(n):
    i=2
    while(i<math.sqrt(n)):
        j=2

        while(j<math.sqrt(i)):
            if(i%j==0):
                break
            if(n%i==0):
                print(i)
                dividers.append(i)
                i=i+1
              
            j=j+1

        i=i+1


euler_tetel(600851475143 )

delete_index=[]
i=2
while(i<len(dividers)):
    k=2
    while(k<dividers[i]):
        if(dividers[i]%k==0):
            delete_index.append(i)
        k=k+1
    i=i+1

print(delete_index)  

delete_index = list(dict.fromkeys(delete_index))


dividers = [i for j, i in enumerate(dividers) if j not in delete_index]        

print(dividers) 
print("vege")

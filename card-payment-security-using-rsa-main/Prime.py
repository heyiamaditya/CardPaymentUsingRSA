import random
import math
def isPrime(num):
    temp=int(math.sqrt(num))
    temp=temp+1
    for i in  range (2,temp) :
        if num%i==0 :
            return 0
        else :
            i+=1
    return 1




def generate_random():
    return (random.randint(2,10000))

while True:
    p=generate_random()
    q=generate_random()
    if isPrime(p)==1 and isPrime(q)==1:
        break

print (p,'\t')
print(q)
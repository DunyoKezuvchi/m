from math import *
def isPrime(n):
    if(n == 1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n % i == 0):
            return False
    return True
a,b,c=map(int,input().split())
sum=0

if(isPrime(a)== True):
    sum+=a
if(isPrime(b) == True):
    sum+=b
if(isPrime(c) == True):
    sum+=c
if(sum == 0):
    print(0)
else:
    print(sum)
    if(isPrime(sum) == True):
        print("Yes")
    else:
        print("No")
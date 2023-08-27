#Generate all primary numbers up to (n)

#Solution
from math import sqrt

def genPrimes(n):
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int(sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False
    for i in range(len(primes)):
        if primes[i] == True:
            print(i, end=' ')

t = int(input())
while t:
    t -= 1
    n = int(input())
    genPrimes(n)

#Time complexity: O(n*Log(Log(n)))
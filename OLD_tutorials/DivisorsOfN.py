#Given an integer (n) find all the possible divisors

#Solution
from math import sqrt

def fun(n):
    div = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            div.add(i)
            div.add(n//i)
    return list(div)


t = int(input())
while t:
    t -= 1
    n = int(input())
    print(*fun(n))

#Time complexity: O(root(n))
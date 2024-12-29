# Given an integer (n) print how many 1's are there in it's binary rappresentation

#Solution

def cntbits(n):
    cnt = 0
    while n:
        cnt+=1
        n = n & (n-1)
    return cnt

t = int(input())
while t:
    t -= 1
    n = int(input())
    print(cntbits(n))

#Time complexity O(log(n))

#Tips: when using bin() function, skip the first 2 digits (0b by using [2:])
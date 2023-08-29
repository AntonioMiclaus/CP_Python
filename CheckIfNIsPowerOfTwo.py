# Given an integer (n) print if it's power of 2 or not.

#Solution

def ispowerof2(n):
    if n <= 0:
        return False
    x = n
    y = not(n & (n-1))
    return x and y

t = int(input())
while t:
    t -= 1
    n = int(input())
    print(ispowerof2(n))

#Time complexity O(1)
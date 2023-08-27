#Given two integers, compute Greatest Common Divisor (GCD) and lowest common multiple (LCM)

#Solution

def gcd(a,b):
    if a == 0:
        return(b)
    return gcd(b%a,a)

def lcm(a,b):
    prod = a * b
    hcf = gcd(a,b)
    return prod // hcf

t = int(input())
while t:
    t -= 1
    n,m = map(int, input().split())
    print(f'gcd: {gcd(n,m)}\nlcm: {lcm(n,m)}')


#Time complexity O(Log(min(a,b)))
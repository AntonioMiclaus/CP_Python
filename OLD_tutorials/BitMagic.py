#Bit Magic tutorial

#Bitwise operators:
# and           &   (used to check even/odd numbers: 2&1 = 0 3&1= 1)
# or            |
# not           ~   (ALT 126 on keyboard)
# xor           ^
# right shift   >>  (divide in power of 2) (ex: n = 200, m = 3 -> n >> m = 200 // 2**3 = 25)
# left shift    <<  (multiply in power of 2) (ex: n = 3, m = 3 -> n << m = 3 * 2**3 = 24)


def evenodd(n):
    if n&1 == 1:
        print('odd')
    else:
        print('even')

def mulpow2(x,y):
    return x << y

def divpow2(x,y):
    return x >> y
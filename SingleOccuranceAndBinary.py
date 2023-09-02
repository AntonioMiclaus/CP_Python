# Given N, return his binary form.

#Solution

def intToBin(n):
    return str(bin(n))[2:]


def binToInt(s):
    return int(s,2)


#kth bit set
#by set we mean that the binary value at position k (starting from right to left) is set to 1 and not to 0
def kthBit(n,k):
    print(str(bin(n))[2:])
    if n & (1 << (k-1)):
        print('Set')
    else:
        print('Not set')

# [5,3,2,3,2,1,5]
# every number occurs twice
# find the number which occurs only once
# remember that n^n == 0 and n^0 == n

def findSingleOccur(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res = res ^ arr[i]
    return res



t = int(input())

while t:
    t-=1
    arr = list(map(int, input().split()))
    print(findSingleOccur(arr))
    #n, k = map(int,input().split())
    #kthBit(n,k)
    #n = int(input())
    #binstring = intToBin(n)
    #integer = binToInt(binstring)
    #print(n ,binstring, integer, n == integer)
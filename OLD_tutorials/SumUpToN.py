#Give an int (n), compute the sum up to (n)
#In competitions usually you are required to find the solution for (t) multiple cases.

#Inputs
#t = number of test cases
#n = int to sum up to 

#Solution

def sum(n):
    n = int(n)
    print(n * (n+1) //2)


#With this loop the code is going to run for every test case.
t = int(input())
while t:
    t -= 1
    sum(input())

#Time complexity: O(1)
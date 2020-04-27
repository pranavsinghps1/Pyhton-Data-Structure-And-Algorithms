#Checking if the kth bit of n is set or not
def checker(n,k):
    if ((n&(1<<(k-1)))!=0):
        print("yes")
    else:
        print("no")

#Another Approach is to move the kth bit to last position and "And" with 1
def RightChecker(n,k):
    if ((n>>(k-1)&1)==1):
        print("yes")
    else:
        print("no")

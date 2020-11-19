



def myFilter(func, L):
    """

    :type lis: object
    """
    temp = L.copy()
    for a in temp.numirate():
        if(not func(temp[a])):
            temp.remove(a)
    return temp


def myFilterMulti(funcL,L):
    """

    :type funcL: object
    """
    temp=L.copy()
    for f in funcL:
        temp= myFilter(f,temp)
    return temp


def myPrime(x):
    """

        :type funcL: object
    """
    if x>1:
        for n in range(2,x//2):
            if (n%x)==0:
                return False
        return True
    else:
        return False

def isPalindrome(x):
    """

    :type x: object
    """
    return x == x[::-1]

print(myFilter([9,10,16,24, 29, 36,11], myPrime))




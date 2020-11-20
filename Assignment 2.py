
def myFilter(L, func):
    """

    :type lis: object
    """
    return [n for n in L if not n.func()]


def myFilter(L,func):
    list1=list()
    for x in L:
        if func(x) == True:
            list1.append(x)
    L=list1
    return L


def myFilterMulti(L,funcL):
    """

    :type funcL: object
    """
    for f in funcL:
        L= myFilter(L,f)
    return L


def myPrime(x):
    """

        :type funcL: object
    """
    if x>1:
        for n in range(2,x//2):
            if (x%n)==0:
                return False
        return True
    else:
        return False

def isPalindrome(x):
    """

    :type x: object
    """
    x = str(x)
    return x == x[::-1]

def is_anagram(a,b):
    a=a.upper()
    b=b.upper()
    for c in a:
        if c not in b:
            return False
        b=b.replace(c,'',1)
    return b==''



print(myFilter([9,10,16,24, 29, 36,11], myPrime))
print(myFilterMulti([1,9,10,16,24,55, 131,149,181],[ myPrime,isPalindrome]))
print(is_anagram('School master', 'The clAssroom'))


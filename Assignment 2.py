def myFilter(func,L):
    temp=L.copy()
    for a in temp.numirate():
        if(not func(temp[a])):
            temp.remove(a)
    return temp

def myFilterMulti(funcL,L):
    temp=L.copy()
    for f in funcL:
        temp= myFilter(f,temp)
    return temp

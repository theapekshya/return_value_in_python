#returning value

def display(a):
    return a     #return 3
d=display(3)      #assign a=3
print(d)


#program to return minimum of two number
def display(a,b):
    if(a<b):
        return a
    elif(b<a):
        return b
    else:
        return 'equal'
x=display(10,20)       #function call
print(x)

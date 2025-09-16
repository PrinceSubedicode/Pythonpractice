a=89    # this is gloabal variable

def fun():
    global a          ## change the value of global variable to 45 using global keyword
    a=45             # this is local variable
    print(a)

fun()       #output: 45
print(a)    # output: 89 if there is no global a

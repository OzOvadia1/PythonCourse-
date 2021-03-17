x = float(input("Enter X: ") )
y = float(input("Enter Y: ") )

#Question A
def exponent (x):
    a = 1
    i = 1
    e = 1
    denom = 1
    
    while i<50 :
        a = a*x
        denom = denom * i
        e = e + a/(denom)
        i = i + 1
    return(e)

def Ln (x):
    if x == 0 :
        return 0
    if x < 0 :
        x = x * -1
    y = 1
    i = 0
    while i<100 :
        y = y + 2*((x-exponent(y))/(x+exponent(y)))
        i = i + 1
    return y
   
def XtimesY (x,y):
    if x == 0 :
        return 0
    result = 0
    result = exponent(y*Ln(x))
 #   result = float('%0.6f' % result)
    if x < 0 and y%2 != 0:
            result = result * -1
    return(result)  


#Question B
def sqrt (x,y):
    if y<=0 and x%2 == 0:
        return 0
    result = 0
    result = exponent((1/x)*Ln(y))
#    result = float('%0.6f' % result)
    return(result)  

#Question C
def calculate (x):
    result = exponent(x)* XtimesY(7,x)* (1/x) * sqrt(x,x)
    result = float('%0.6f' % result)
    return (result)


    
    
    
    
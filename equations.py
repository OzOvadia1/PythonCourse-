x = float(input("Enter X: ") )
y = float(input("Enter Y: ") )



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
    y = 1
    i = 0
    while i<100 :
        i = 1
        y = y + 2*((x-exponent(y))/(x+exponent(y)))
        i = i + 1
    return y
print(Ln(x))
   
#def XtimesY (x,y):
 #   result = 0
  #  result = exponent(y*Ln(x))
   # return(result)  
  
#print(XtimesY(x,y))
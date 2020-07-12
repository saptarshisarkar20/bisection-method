# bisection-method
"""You're given a function 
x = 2x² + 5logx - √x/π 
Using Bisection method 
find the root of this equation using Numpy . 
The roots of this equation should be correct upto 5 decimal places."""
# so this is our question... let,s solve...
#1st define a function which defines the function in question
# before that import numpy

import numpy as np
def f(x): #takes only one argument x;
    return (2*(x**2)+5*(np.log(x))-(np.sqrt(x)/np.pi))
#our function is completed
#now use the bisection method
#here the tollerance is upto 5 decimal pleaces
def bisection(a,b): #here a,b is the uppr and lower limit
    a_f = f(a)
    b_f = f(b)
    c = (a+b)/2 #according to bisection method
    tol = 0.000001
    while abs(f(c)) > tol : # here we are using the absolute value only to check
        if f(a)*f(c)>0 :                                #tollerance 
            a = c
        else :
            b = c                # following the rule of bisection method
        c = (a+b)/2
    return c
    #our bisection function is also completed
    #let's run the program using the range u want to run

ans = bisection(5,0) #here i am using the range of 5 to -5 // just make a correcction
print("The root is: ",ans)

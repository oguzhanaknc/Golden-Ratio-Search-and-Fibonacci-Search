import math
PHI = 1.6180339887499
PSI = -0.61803398871499
REVERSE_SQUARE_ROOT_FIVE = 0.447213595499958


def fibonacci_number(n):
    return (PHI**n - PSI**n)*REVERSE_SQUARE_ROOT_FIVE


def calculate(goal_function, a, b, epsilon,maxiter):
    x = 0
    n = 100
    iterCount = 0
    while ((b - a) > epsilon or n != 1) and maxiter > iterCount:
        print("iterasyon: " ,  iterCount , "\n")

        lamda = a + (b - a)*(fibonacci_number(n-2)/fibonacci_number(n))
        mu = a + (b - a)*(fibonacci_number(n-1)/fibonacci_number(n))

        if goal_function(lamda) <= goal_function(mu):
            b = mu
            x = lamda
        else:
            a = lamda
            x = mu

        n -= 1
        print(a, " < x < ",b)

    if n == 1:
        print("iterasyon bitti x = ",(mu + lamda) / 2 , " fonksiyon değeri = ", f((mu + lamda) / 2),"\n")
        return
    print("iterasyon bitti x = ",x , " fonksiyon değeri = ", f(x),"\n")

    

def f(x):
    return math.exp(x)-5*x

calculate(goal_function=f,a=1,b=2,epsilon=0.01,maxiter=10)
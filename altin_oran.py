PHI = 1.618
REVERSED_PHI = 1/PHI


def calculate(goal_function, a, b, epsilon,maxiter):
    x = 0
    iterCount = 0
    while (b - a) > epsilon and iterCount < maxiter:
        print("iterasyon: " ,  iterCount , "\n")
        lamda = b - (b - a)*REVERSED_PHI
        mu = a + (b - a)*REVERSED_PHI
       

        if goal_function(lamda) <= goal_function(mu):
            b = mu
            x = lamda
        else:
            a = lamda
            x = mu
        print(a, " < x < ",b)
        iterCount+=1
    print("iterasyon bitti x = ",x , " fonksiyon değeri = ", f(x),"\n")


def f(x):
    return 3*(x**3)+(x**2)−1

calculate(goal_function=f,a=0,b=4,epsilon=0.2,maxiter=3)
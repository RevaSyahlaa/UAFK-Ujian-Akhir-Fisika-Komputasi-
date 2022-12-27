def Trapezoid(a,b,f):
    n = 1000
    def trapezoid(f,a,b,n=100):
        h=(b-a)/n
        sum = 0.0
        for i in range (1,n):
            x = a+i*h
            sum = sum +f(x)
        integral = (h/2)*(f(a)+2*sum+f(b))
        return integral
    integral = trapezoid(f,a,b,n)
    print(a,",",b,",",round(integral,2))


for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 2*x)

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 2*x+2 )

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 2*x+4)

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 4*x+6 )

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 6*x+8)

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 8*x+10)

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 10*x+12)

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 12*x+14)

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 14*x+12)

for i in range(0,5):
    Trapezoid(i+1,i+2,lambda x: 20*x+40)

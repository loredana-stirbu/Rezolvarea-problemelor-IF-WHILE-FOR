from math import log
m=int(input("Introduceti un numar m:"))
n=int(input("Introduceti un numar n care sa fie mai mare ca m:"))
i=log(m,n)
a=int(i)
if i-a==0:
    print("n este puterea lui m")
else:
    print("n nu este putere lui m")   
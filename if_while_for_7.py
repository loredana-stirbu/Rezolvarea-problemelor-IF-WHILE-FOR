n = int(input("introduceti virsta lui Mihai:"))
d=1
if n<20:
    for i in range(1, n+1 ):
        if i==1:
            d=1
        else:
            d=(d*2)+i
print("La virsta de " ,n, "an(i) Mihai a primit " ,d, "dolar(i)") 
if n==7:
    print("La virsta de",n,"ani cadoul lui Mihai depaseste suma de 100 de dolari")    
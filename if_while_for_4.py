from fractions import Fraction
num1 = int(input("Scrieti numărătorul: "))
numit1 = int(input("Scrieti numitorul: "))
num2 = int(input("Scrieti numărătorul: "))
numit2 = int(input("Scrieti numitorul: "))
adunarea = (Fraction(num1,numit1)+Fraction(num2,numit2))
înmulțirea = (Fraction(num1,numit1)*Fraction(num2,numit2))
print("adunarea =",adunarea)
print("înmulțirea =",înmulțirea)
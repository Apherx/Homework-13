def quadraticformula1(a,b,c):
    x = (-b+(b**2 -4*a*c)**0.5) / 2*a
    return (x)
def quadraticformula2(a,b,c):
    x = (-b-(b**2 -4*a*c)**0.5) /2*a
    return (x)

a = float(input("What is the value of a?: "))
b = float(input("What is the value of b?: "))
c = float(input("What is the value of c?: "))
print("The roots of the equation are: ")
print( quadraticformula1(a,b,c) )
print(quadraticformula2(a,b,c) )
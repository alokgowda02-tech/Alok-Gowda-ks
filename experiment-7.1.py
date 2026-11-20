def factorial(n):
    if n<0:
        return None
    result = 1
    for i in range(2, n + 1):
       result *= i
    return result

def simple_interest(principal, time, rate=5.0):
 return (principal * time * rate) / 100

square = lambda x: x * x
n = int(input("Enter a number for factorial:"))
fact = factorial(n)
if fact is None:
    print("Factorial is not defined for negative numbers.")

else:
    print("Factorial =", fact)

p = float(input("Enter principal amount:"))
t = float(input("Enter time in years:"))
print("Simple Interest (default rate 5%) =", simple_interest(p, t))

x = float(input("Enter a number to find its square:"))
print("Square =", square(x)) 
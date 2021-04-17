n = eval(input("Enter and integer: "))
product = 1

for num in range(1,n+1):
    product *= num

print("Factorial of "+str(n)+ " s: ", product)
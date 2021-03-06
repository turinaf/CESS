import math
def factorial(number):
    product = 1
    for i in range(1, number+1):
        product *= i
    return product
# print(factorial(3))

def recursive_factorial(number):
    if number == 0:
        return 1
    return number * recursive_factorial(number-1)

def is_prime(number):
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i== 0:
            return False
    return True


if __name__ == '__main__': #Checking if the this file is being run from here
    print(is_prime(19783))
    # print(recursive_factorial(3))

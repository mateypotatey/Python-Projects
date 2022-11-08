"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below."""

def primality(num):
    if num == 1:
        return True
    else:
        is_prime = False
        divisors = 0
        for i in range (1, num + 1):
            if num % i == 0:
                divisors += 1

        if divisors == 2:
            is_prime = True
        return is_prime


for i in range(1, 50):
    print(i, primality(i))

#simplified version I found online.
def prime(n):
    if n % n == 0 and n % 2 != 0 and n % 3 != 0:
        return True
    else:
        return False

for i in range(1,50):
    print(i, prime(i))
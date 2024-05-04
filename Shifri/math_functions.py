import random

def miller_rabin(n, k=10):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def ReverseEuclideanAlgorithm(num1, num2):
    ostatki = []
    r = num1 % num2
    ostatki.append([1, -(num1 // num2)])
    i = 0
    while r != 0:
        num1 = num2
        num2 = r
        r = num1 % num2
        divisor = num1 // num2
        if i == 0:
            ostatki.append([-divisor * ostatki[i][0], 1 - divisor * ostatki[i][1]])
        else:
            ostatki.append([ostatki[i-1][0] - divisor * ostatki[i][0], ostatki[i-1][1] - divisor * ostatki[i][1]])
        i += 1
    if len(ostatki) > 1:
        return ostatki[-2]
    else:
        return [0, 0]

def EuclideanAlgorithm(num1, num2):
    r = num1 % num2
    while r != 0:
        num1 = num2
        num2 = r
        r = num1 % num2
    result = num2
    return result

def fast_modular_exponentiation(base, exponent, modulus):
    result = 1
    base %= modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus

    return result
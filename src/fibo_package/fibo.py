import math

def fibo(n):
    return round(((math.pow(((1 + math.sqrt(5)) / 2), n) - math.pow(((1 - math.sqrt(5)) / 2), n)) / math.sqrt(5)))
print(fibo(50))
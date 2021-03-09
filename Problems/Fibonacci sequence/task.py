

def fibonacci(zahl):
    a, b = 0, 1
    i = 0
    while i < zahl:
        yield a
        a, b = b, a + b
        i += 1



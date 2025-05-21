import math

def expt(a, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return a ** expt(a, math.sqrt(n))
    else:
        return a ** expt(a, n - 1)



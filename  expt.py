def expt(a, n):
    if n == 0:
        return 1

    return a ** expt(a, n - 1)
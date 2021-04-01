def Factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * Factorielle(n-1)

print(Factorielle(3))
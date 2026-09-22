

def F(A, iter):
    A = str(A)
    if len(A) == 1: return iter

    Mult = 1
    for i in A:
        Mult *= int(i)

    return F(Mult, iter + 1)


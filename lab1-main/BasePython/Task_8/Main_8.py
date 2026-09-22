
def F(A):
    A = str(A)

    if len(A) % 2 == 0:
        N1 = A[:int(len(A) / 2)]
        N2 = A[int(len(A) / 2):]
    else:
        N1 = A[:int((len(A)-1) / 2)]
        N2 = A[int((len(A)+1) / 2):]

    return sum([int(i) for i in N1]) == sum([int(i) for i in N2])


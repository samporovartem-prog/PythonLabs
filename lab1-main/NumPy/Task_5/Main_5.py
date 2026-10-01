import numpy as np



def chess(m, n, a, b):
    M = []

    for i in range(m):
        M.append([])
        for j in range(n):
            if (i + j) % 2 == 0: M[-1].append(a)
            else: M[-1].append(b)

    return np.array(M)

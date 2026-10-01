import numpy as np



def OHE(V):
    M = []

    for i in V:
        M.append([])

        for j in range(max(V) + 1):
            if i == j: M[-1].append(1)
            else: M[-1].append(0)

    return np.array(M)


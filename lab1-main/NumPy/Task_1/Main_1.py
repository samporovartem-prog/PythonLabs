import numpy as np
import matplotlib.pyplot as plt



def sum_prod(X, V):
    '''
    X - матрицы (n, n)
    V - векторы (n, 1)
    Гарантируется, что len(X) == len(V)
    '''

    L = []
    for i in range(len(X)):
        L.append(X[i].dot(V[i]))

    S = np.zeros((len(V[0]), len(V[0])))
    for i in range(len(X)):
        S += L[i]

    return S


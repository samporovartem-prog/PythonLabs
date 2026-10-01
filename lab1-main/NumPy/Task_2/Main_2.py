import numpy as np
import matplotlib.pyplot as plt



def binarize(M, threshold=0.5):

    NewM = []
    for i in M:
        NewM.append([])

        for j in i:
            if j > threshold: NewM[-1].append(1)
            else: NewM[-1].append(0)

    return np.array(NewM)


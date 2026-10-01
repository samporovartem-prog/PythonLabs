import numpy as np



def unique_rows(M):

    UniqM = []
    for i in M:
        UniqM.append([])

        for j in i:
            if not(j in i): UniqM[-1].append(j)

    return UniqM

def unique_columns(M):

    UniqM = []

    for x in range(len(M[0])):
        UniqM.append([])
        Column = M[:, x]

        for j in Column:
            if not(j in Column): UniqM[-1].append(j)
            else: UniqM.append(None)
    
    return np.array(UniqM).T
    
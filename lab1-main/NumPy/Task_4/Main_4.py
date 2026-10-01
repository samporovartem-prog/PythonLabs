import numpy as np
np.random.seed(123456789)



def matrix_statistics(m, n):
    return MatrixStatistics(m, n)


class MatrixStatistics():

    def __init__(self, m, n):
        self.M = np.random.normal(loc = 0, scale = 5, size = (m, n))
        self.MidRow = self.MidRow_()
        self.MidColumn = self.MidColumn_()
        self.DispRow = self.DispRow_()
        self.DispColumn = self.DispColumn_()        


    def MidRow_(self):
        midR = []

        for i in self.M:
            midR.append([])
            midR[-1].append(float(sum(i)) / len(i))

        return midR

    def MidColumn_(self):
        midC = []

        for i in range(len(self.M[0])):
            midC.append(float(sum(self.M[:, i])) / len(self.M))

        return midC

    def DispRow_(self):
        dispR = []
        
        for i in self.M:
            dispR.append([])

            mid = float(sum(i)) / len(i)
            D = sum( [(float(j) - mid)**2 for j in i] ) / len(i)

            dispR[-1].append(D)

        return dispR

    def DispColumn_(self):
        dispC = []
        
        for x in range(len(self.M)):
            i = self.M[:, x]
            
            mid = float(sum(i)) / len(i)
            D = sum( [(float(j) - mid)**2 for j in i] ) / len(i)

            dispC.append(D)

        return dispC
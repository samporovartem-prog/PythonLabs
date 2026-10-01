import numpy as np



def analyze_time_series(series):
    return TimeSeriesStatistics(series)


class TimeSeriesStatistics():

    def __init__(self, S):
        self.S = S # Series

        self.MatExpect = self.MatExpect_()
        self.Dispersion = self.Dispersion_()
        self.SquareDev = self.SquareDev_()
        self.LocalMax = self.LocalMax_()
        self.LocalMin = self.LocalMin_()
        self.MoveMid = self.MoveMid_(3)


    def MatExpect_(self):
        P = [self.S.count(i) for i in self.S]

        M = sum([self.S[i] * P[i] for i in range(len(self.S))])
        return M

    def Dispersion_(self):
        mid = sum(self.S) / len(self.S)
        
        D = sum( [(i - mid)**2 for i in self.S] ) / len(self.S)
        return D

    def SquareDev_(self):
        mid = sum(self.S) / len(self.S)

        SD = (sum( [(i - mid)**2 for i in self.S] ) / len(self.S))**0.5
        return SD

    def LocalMax_(self):
        Lmax = []

        for i in range(1, len(self.S) - 2):
            if self.S[i - 1] < self.S[i] > self.S[i + 1]: Lmax.append(i)

        return Lmax

    def LocalMin_(self):
        Lmin = []

        for i in range(1, len(self.S) - 2):
            if self.S[i - 1] > self.S[i] < self.S[i + 1]: Lmin.append(i)

        return Lmin

    def MoveMid_(self, P):
        newS = []

        for i in range(len(self.S) - 1):

            q = []
            for j in range(i - P, i + P + 1):
                if (j < 0) or (j >= len(self.S)): continue
                q.append(self.S[j])

            newS.append( sum(q) / len(q) )

        return(newS)


analyze_time_series([1, 2, 3, 4, 5, 6])
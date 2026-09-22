
def F(string = str):
    S1 = [i for i in string]
    S2 = list(set(S1))

    if len(S1) == len(S2): return True
    else: return False


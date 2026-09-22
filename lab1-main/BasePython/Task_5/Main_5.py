
def mse(V1, V2):
    if (sum([i**1 for i in V1])**0.5 != sum([i**1 for i in V2])**0.5) or len(V1) != len(V2):
        return None

    return (sum([(V1[i] - V2[i])**2 for i in range(len(V1))]) / len(V1))**0.5


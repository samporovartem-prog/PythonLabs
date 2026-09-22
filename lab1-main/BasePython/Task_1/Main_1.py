
def F(string = str):
    C = 0

    for i in ['a', 'e', 'i', 'o', 'u']:
        C += string.lower().count(i)

    return C


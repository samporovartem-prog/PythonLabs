
def pyramid(N):

    k = 0
    S = 0
    while True:
        k += 1
        S += k**2

        if S == N: return k
        if S > N: return 'It is impossible'



def F(A):
    PrimeNum = [2]
    Count = {2: 0}


    while True:
        if A == 1: break

        # Проверка на делимость
        while True:
            if A % PrimeNum[-1] != 0: break

            Count[PrimeNum[-1]] += 1
            A /= PrimeNum[-1]

        # Вычисление след. простого числа
        n = PrimeNum[-1]
        while True:
            n += 1

            j = 0
            for i in PrimeNum:
                if n % i == 0:
                    j = 1
                    break

            if j == 0:
                PrimeNum.append(n)
                Count[n] = 0
                break

    # Вывод рез-та
    Output = ''
    for n in list(Count.keys()):
        if Count[n] == 0: continue
        if Count[n] == 1: Output += f'({n})'
        else: Output += f'({n}**{Count[n]})'

    return Output


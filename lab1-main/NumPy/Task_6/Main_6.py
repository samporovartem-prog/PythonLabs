import matplotlib.pyplot as plt



def draw_ellipse(a, b, m, n, bd_color, bg_color):
    fig, ax = plt.subplots(figsize = (m, n))
    ax.set_title('ellipse')
    ax.set_aspect('equal', adjustable='box')

    ax.plot([0, 0], [-max(a, b), max(a, b)], color = 'gray', linewidth = 1)
    ax.plot([-max(a, b), max(a, b)], [0, 0], color = 'gray', linewidth = 1)

    Lx, Ly = [], []
    for i in range(-a * 10, a * 10 + 1):
        x = i / 10
        Lx.append(x)
        Ly.append( b * (1 - x**2 / a**2)**0.5 )

    for i in Lx[::-1]: Lx.append(i)
    Lx.append(Lx[0])

    for i in Ly[::-1]: Ly.append(-i)
    Ly.append(Ly[0])


    ax.fill(Lx, Ly, color = bg_color,)
    ax.plot(Lx, Ly, color = bd_color, linewidth = 3)

    plt.show()


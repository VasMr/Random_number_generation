import matplotlib.pyplot as plt
from numpy import pi, arange, sin, array


def rand_generator(a, b, N=1, seed=1, integer=True):
    rands = []
    if integer:
        for i in range(N):
            num = int(a + (b - a) * (abs(hash(str(hash(str(seed) + str(i + 1)))))) / 10 ** 19)
            rands.append(num)
        return rands
    else:
        for i in range(N):
            num = (a + (b - a) * (abs(hash(str(hash(str(seed) + str(i + 1)))))) / 10 ** 19)
            rands.append(num)
        return rands


def graph():
    fig, axs = plt.subplots(nrows=2, ncols=1)
    fig.suptitle('Distribution of random generation results')

    axs[0].plot([i for i in range(-10, 11)], [i for i in range(-10, 11)], color='black')
    axs[0].plot([i for i in range(-10, 11)], [i for i in range(-5, 16)], linestyle='dashed', color='red', linewidth=1)
    axs[0].plot([i for i in range(-10, 11)], [i for i in range(-15, 6)], linestyle='dashed', color='red', linewidth=1)
    axs[0].plot([i for i in range(-10, 10)],
                [rand_generator(-15 + i, -5 + i, 20, integer=True)[i] for i in range(0, 20)],
                color='green', marker='o')
    axs[0].set_title('Generated int numbers')

    x_m = arange(1, 5 * pi, 0.1)
    y_m = sin(x_m)

    x_1 = x_m
    y_1 = sin(x_m) + 2

    x_2 = x_m
    y_2 = sin(x_m) - 2

    x_d = x_m = arange(1, 5 * pi, 0.1)
    print(len(x_d))
    y_disp = array(rand_generator(-2, 2, 148, integer=False))
    y_d = y_m + y_disp

    axs[1].plot(x_m, y_m, color='black')
    axs[1].plot(x_1, y_1, linestyle='dashed', color='red', linewidth=1)
    axs[1].plot(x_2, y_2, linestyle='dashed', color='red', linewidth=1)
    axs[1].plot(x_d, y_d, color='green', marker='o')
    axs[1].set_title('Generated real numbers')
    plt.show()


def rand_generator(a, b, N=1, seed=1, integer=True):
    rands = []
    if integer:
        for i in range(N):
            num = int(a + (b - a) * (abs(hash(str(hash(str(seed) + str(i + 1)))))) / 10 ** 19)
            rands.append(num)
        return rands
    else:
        for i in range(N):
            num = (a + (b - a) * (abs(hash(str(hash(str(seed) + str(i + 1)))))) / 10 ** 19)
            rands.append(num)
        return rands


graph()

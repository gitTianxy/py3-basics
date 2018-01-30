import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.exp(-x)
y3 = np.sin(4 * np.pi * x)
y4 = np.exp(-2 * x)


def plot_by_axes():
    fig = plt.figure()
    # plot A
    ax1 = fig.add_axes([0.1, 0.1, 0.4, 0.7])
    l1, l2 = ax1.plot(x, y1, 'rs-', x, y2, 'go')
    fig.legend((l1, l2), ('Line 1', 'Line 2'), 'upper left', borderpad=1, handlelength=2, handleheight=2,
               labelspacing=2, fontsize='8', markerscale=0.8)
    # plot B
    ax2 = fig.add_axes([0.55, 0.1, 0.4, 0.7])
    l3, l4 = ax2.plot(x, y3, 'yd-', x, y4, 'k^')
    fig.legend((l3, l4), ('Line 3', 'Line 4'), 'upper right')

    plt.show()


def subplot_demo():
    fig = plt.figure()
    # plot A
    ax1 = fig.add_subplot(1, 2, 1)
    l1, l2 = ax1.plot(x, y1, 'rs-', x, y2, 'go')
    fig.legend((l1, l2), ('Line 1', 'Line 2'), 'upper left', borderpad=1, handlelength=2, handleheight=2,
               labelspacing=2, fontsize='8', markerscale=0.8)
    # plot B
    ax2 = fig.add_subplot(1, 2, 2)
    l3, l4 = ax2.plot(x, y3, 'yd-', x, y4, 'k^')
    fig.legend((l3, l4), ('Line 3', 'Line 4'), 'upper right')

    plt.show()


if __name__ == '__main__':
    plot_by_axes()
    # subplot_demo()

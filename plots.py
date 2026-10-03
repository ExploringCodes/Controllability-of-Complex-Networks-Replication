import numpy as np
import matplotlib.pyplot as plt


def plot_nd(gamma=3, k_min=0, k_max=20, points=200):
    k = np.linspace(k_min, k_max, points)
    n_D = np.exp(-0.5 * (1 - 1 / (gamma - 1)) * k)
    plt.plot(k, n_D)
    plt.xlabel('Average degree <k>')
    plt.ylabel('n_D')
    plt.show()


if __name__ == '__main__':
    plot_nd(gamma=2.2, k_min=0, k_max=20)

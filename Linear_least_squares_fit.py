import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
from numpy.linalg import pinv

def linear_least_squares_fit():

    x_r1 = []
    x_r2 = []

    x_array = np.zeros((2, 50))
    y_array = []

    u = (1 - (-1)) * random.sample(50) - 1
    u.reshape(50, 1)

    for i in range(0, 50):
        x_r1.append(1)

    for i in range(1, 51):
        x_r2.append(i)
        y = i + u[(i - 1)]
        y_array.append(y)

    x_array[0] = x_r1
    x_array[1] = x_r2
    print("x_array:",x_array)
    print("done")

    x_matrix = np.matrix(np.array(x_array))
    print(x_matrix)
    y_matrix = np.matrix(np.array(y_array))

    x_pseudo = pinv(x_matrix)
    w_minimum = y_matrix * x_pseudo

    w_array = []
    w_array.append(w_minimum[0, 0])
    w_array.append(w_minimum[0, 1])

    for i in range(0, 50):
        plt.plot(x_r2[i], y_array[i], 'ro')

    y1 = w_array[0]
    y2 = (w_array[0] + 50 * w_array[1])

    x_plot = [0, 50]
    y_plot = [y1, y2]

    plt.plot(x_plot, y_plot, 'g-')
    plt.show()
    plt.xlim(0, 50)
    plt.ylim(0, 51)

linear_least_squares_fit()

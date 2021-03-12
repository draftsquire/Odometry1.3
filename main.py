import math

import numpy as np
import statistics
from math import cos, sin, pi


def data_reader():
    M, N, a, h = map(float, input().replace(',', '.').split(" "))
    M = int(M)
    N = int(N)
    K = int(input())
    data = np.zeros(shape=(K * M, N))

    for i in range(K * M):
        data[i] = list(map(int, input().replace(',', '.').split(" ")))
    return M, N, a, h, K, data


def distance_counter(M, N, a, h, K, odometry_data):
    b = h * math.tan(a / 2) * K / (N * 0.5)
    data_old = odometry_data[0:M]
    offset = []
    for i in range(2, K + 1):
        data = odometry_data[(i - 1) * M:i * M]
        for j in range(M - 1, 1, -1):
            if (data[j] == data_old[M - 1]).all() and (data[j - 1] == data_old[M - 2]).all():  ## this shit
                offset.append(M - j - 1)
                print(M - j - 1)
            else:
                continue
            break
        data_old = data
    print(round(max(offset) * b, 2))
    return 0


if __name__ == '__main__':
    M, N, a, h, K, odometry_data = data_reader()
    # переводим из градусов в радианы
    a = a * pi / 180
    print(odometry_data)
    distance_counter(M, N, a, h, K, odometry_data)

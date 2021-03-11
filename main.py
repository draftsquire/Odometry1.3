import numpy as np
from math import cos, sin,pi
import matplotlib.pyplot as plt
def data_reader():
    M, N, a, h = map(float, input().replace(',', '.').split(" "))
    M = int(M)
    N = int(N)
    K = int(input())
    data= np.zeros(shape=(K*M,N))


    for i in range(K*M):
        data[i] = list(map(int,input().replace(',', '.').split(" ")))
    return M,N,a,h,K,data

def distance_counter (M,N,a,h,K, odometry_data):
    #длина/ширина зоны обзора
    b  = 2*h / cos(a/2)
    print("длина/ширина зоны обзора: ", b)

    image = np.zeros(shape=(M, N))
    for i in range(1,K+1):
        print(i)
        plt.imshow(odometry_data[(i-1)*M:i*M])
        plt.show()
    plt.gray()

    return 0

if __name__ == '__main__':
    M,N,a,h,K, odometry_data = data_reader()
    #переводим из градусов в радианы
    a = a* pi /180
    print(odometry_data)
    distance_counter(M,N,a,h,K, odometry_data)
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import time

# install matplotlib
# python -m pip install -U matplotlib

def random_matrix_maken(N, M):
    """
    Deze functie maakt een matrix met alle dipolen een random spin up (1)
    of spin down(0).
    """
    matrix = np.zeros((N,M))

    for y in range(N):
        for x in range(M):
            random_spin = int(random.random()*2)
            if random_spin == 0:
                random_spin = -1
            matrix[y][x] = random_spin
    return matrix


def grid_maken(M, N):
    matrix = np.zeros((M,N))

    matrix[0][0]
    return matrix


def plot_orgineel(M, N):
    """
    Deze functie geeft 1 plot van het Ising model. De functie 'iteration' wordt
    een bepaald aantal stappen doorlopen tot dat elk dipole punt in de matrix vele
    keren de kans heeft gehad om de orientitie te flippen.
    """
    matrix = grid_maken(M, N)

    # Plot
    plt.figure()
    plt.imshow(matrix, interpolation='none', vmin = -1 , vmax = 1)
    plt.xlabel('x-as')
    plt.ylabel('y-as')
    plt.show()

M = 6
N = 6
plot_orgineel(M, N)

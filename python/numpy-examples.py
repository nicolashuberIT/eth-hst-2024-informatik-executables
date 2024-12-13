#########################
# Wie in C6 gezeigt
#########################

import numpy as np

arr = np.array([1, 2, 3, 4, 5], int)                # Array erstellen
print(arr)                                          # >>> [1 2 3 4 5]

zeros = np.zeros((2, 3))                            # Array mit Nullen
ones = np.ones((2, 3))                              # Array mit Einsen
print(zeros)                                        # >>> [[0. 0. 0.] [0. 0. 0.]]
print(ones)                                         # >>> [[1. 1. 1.] [1. 1. 1.]]

rand_arr = np.random.rand(2, 3)                     # Array mit Zufallszahlen zwischen 0 und 1
rand_int_arr = np.random.randint(0, 10, (2, 3))     # Array mit Zufallszahlen zwischen 0 und 10
print(rand_arr)                                     # >>> [[0.5488135  0.71518937 0.60276338] [0.54488318 0.4236548  0.64589411]]
print(rand_int_arr)                                 # >>> [[3 7 9] [3 7 2]]

print(arr + 2)                                      # >>> [3 4 5 6 7]
print(arr * 2)                                      # >>> [2 4 6 8 10]
print(arr ** 2)                                     # >>> [1 4 9 16 25]

a = np.array([[1, 2], [3, 4]])                      # Matrix erstellen für Matrixmultiplikation
b = np.array([[5, 6], [7, 8]])                      # Matrix erstellen für Matrixmultiplikation
print(np.dot(a, b))                                 # >>> [[19 22] [43 50]] (Matrixmultiplikation)

print(a.T)                                          # >>> [[1 3] [2 4]] (Transponierte Matrix)                   

print(np.sum(arr))                                  # >>> 15 (Summe)
print(np.mean(arr))                                 # >>> 3.0 (Durchschnitt)
print(np.min(arr))                                  # >>> 1 (Minimum)
print(np.max(arr))                                  # >>> 5 (Maximum)
print(np.sort(arr))                                 # >>> [1 2 3 4 5] (aufsteigend sortiert)

print(arr[0])                                       # >>> 1 (Indexierung)
print(a[1, 1])                                      # >>> 4 (Indexierung)
print(arr[1:4])                                     # >>> [2 3 4] (Slicing)
print(a[:, 1])                                      # >>> [2 4] (Spalte) (Slicing)
print(a[1, :])                                      # >>> [3 4] (Zeile) (Slicing)

print(arr.size)                                     # >>> 5 (Grösse)
print(arr.shape)                                    # >>> (5,) (Form)

for element in arr:                                 # Iteration über Arrays
    print(element, end=",")                         # >>> 1,2,3,4,5,

matrix = np.zeros((100, 100))                       # List comprehension
matrix[1:100, 1:100] = 5
print(matrix)
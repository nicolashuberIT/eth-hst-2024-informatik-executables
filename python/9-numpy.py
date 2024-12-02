import numpy as np

# Array erstellen
arr = np.array([1, 2, 3, 4, 5], int)
print(arr)  # >>> [1 2 3 4 5]

# Array mit Nullen und Einsen
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
print(zeros)  # >>> [[0. 0. 0.] [0. 0. 0.]]
print(ones)   # >>> [[1. 1. 1.] [1. 1. 1.]]

# Array mit Zufallszahlen
rand_arr = np.random.rand(2, 3)
rand_int_arr = np.random.randint(0, 10, (2, 3))
print(rand_arr)
print(rand_int_arr)

# Grundlegende Operationen
print(arr + 2)  # >>> [3 4 5 6 7]
print(arr * 2)  # >>> [2 4 6 8 10]
print(arr ** 2) # >>> [1 4 9 16 25]

# Matrixmultiplikation
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))  # >>> [[19 22] [43 50]]

# Transponieren
print(a.T)  # >>> [[1 3] [2 4]]

# Summen und Mittelwerte
print(np.sum(arr))  # >>> 15
print(np.mean(arr)) # >>> 3.0

# Indexierung und Slicing
print(arr[0])       # >>> 1
print(a[1, 1])      # >>> 4
print(arr[1:4])     # >>> [2 3 4]
print(a[:, 1])      # >>> [2 4] (Spalte)
print(a[1, :])      # >>> [3 4] (Zeile)

# Größe und Form
print(arr.size)     # >>> 5
print(arr.shape)    # >>> (5,)

# Weitere Funktionen
print(np.min(arr))  # >>> 1
print(np.max(arr))  # >>> 5
print(np.sort(arr)) # >>> [1 2 3 4 5]

# Iteration über Arrays
for element in arr:
    print(element, end=",")  # >>> 1,2,3,4,5,

# List comprehension
matrix = np.zeros((100, 100))
matrix[1:100, 1:100] = 5
print(matrix)
#########################
# Wie in C5 gezeigt
#########################

import matplotlib.pyplot as plt

# Basisdaten

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

data_histogram = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
data_boxplot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Einfache Linie plotten
plt.plot(x, y)
plt.show()  # Zeigt den Plot

# Titel und Achsenbeschriftungen hinzufügen
plt.plot(x, y)
plt.title('Einfacher Plot')
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.show()

# Mehrere Linien plotten
plt.plot(x, y, label='y = f(x)')
plt.plot(x, y2, label='y2 = g(x)')
plt.legend()
plt.show()

# Balkendiagramm
plt.bar(x, y)
plt.show()

# Histogramm
plt.hist(data_histogram, bins=4)
plt.show()

# Streudiagramm
plt.scatter(x, y)
plt.show()

# Boxplot
plt.boxplot(data_boxplot)
plt.show()
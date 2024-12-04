#########################
# Wie in C8 gezeigt
#########################

def linear_search(num_list, target):
  n = len(num_list)

  for i in range(0, n):                               # Durchlauf der gesamten Liste
    if num_list[i] == target:                         # Überprüfen, ob das aktuelle Element das Ziel ist
      return i                                        # Ziel gefunden, Index zurückgeben

  return -1                                           # Ziel nicht gefunden

#########################
# Wie in C9 gezeigt
#########################

def binary_search(num_list, target):
    left, right = 0, len(num_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if num_list[mid] == target:                   # Überprüfen, ob das mittlere Element das Ziel ist
            return mid                                # Ziel gefunden, Index zurückgeben

        elif num_list[mid] < target:                  # Wenn das Ziel größer ist, ignorieren wir die linke Hälfte
            left = mid + 1

        else:                                         # Wenn das Ziel kleiner ist, ignorieren wir die rechte Hälfte
            right = mid - 1

    return -1                                         # Ziel nicht gefunden

# Anwendung

target = 25
num_list = [64, 34, 25, 12]                            # Numerische Liste (unsortiert)
num_list_sorted = [12, 25, 34, 64]                     # Sortierte numerische Liste (wichtig für die binäre Suche)
print(linear_search(num_list, target))                 # >>> 2
print(binary_search(num_list_sorted, target))          # >>> 1

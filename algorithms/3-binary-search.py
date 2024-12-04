def binary_search(num_list, target):
    left, right = 0, len(num_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if num_list[mid] == target:             # Überprüfen, ob das mittlere Element das Ziel ist
            return mid                          # Ziel gefunden, Index zurückgeben

        elif num_list[mid] < target:            # Wenn das Ziel größer ist, ignorieren wir die linke Hälfte
            left = mid + 1

        else:                                   # Wenn das Ziel kleiner ist, ignorieren wir die rechte Hälfte
            right = mid - 1

    return -1                                   # Ziel nicht gefunden

num_list = [12, 25, 34, 64]                     # Sortierte numerische Liste (wichtig für die binäre Suche)
target = 25

print(binary_search(num_list, target))          # >>> 1
def linear_search(num_list, target):
  n = len(num_list)

  for i in range(0, n):                   # Durchlauf der gesamten Liste
    if num_list[i] == target:             # Überprüfen, ob das aktuelle Element das Ziel ist
      return i                            # Ziel gefunden, Index zurückgeben

  return -1                               # Ziel nicht gefunden

num_list = [64, 34, 25, 12]               # Numerische Liste (unsortiert)
target = 25

print(linear_search(num_list, target))    # >>> 2
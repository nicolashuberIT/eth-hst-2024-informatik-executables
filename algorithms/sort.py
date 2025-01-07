# pylint: disable=expression-not-assigned

#########################
# Wie in C7
#########################


def bubble_sort_asc(num_list):
    n = len(num_list)

    for i in range(0, n):  # Repräsentiert jeden vollständigen Listendurchlauf

        for j in range(
            0, n - i - 1
        ):  # Listendurchlauf von Index 0 bis zum kleinsten unsortierten Element n-i-1

            if (
                num_list[j] > num_list[j + 1]
            ):  # Element mit nächst grösserem vergleichen und geg. austauschen
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    return num_list


def bubble_sort_desc(num_list):
    n = len(num_list)

    for i in range(0, n):
        for j in range(0, n - i - 1):

            if num_list[j] < num_list[j + 1]:  # einziger Unterschied zu bubble_sort_asc
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    return num_list


# Anwendung

unsorted_list = [64, 34, 25, 12]  # Unsortierte numerische Liste
print(bubble_sort_asc(unsorted_list))  # >>> [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort_desc(unsorted_list))  # >>> [90, 64, 34, 25, 22, 12, 11]

#########################
# Erweiterung gemäss Coding Bazar
#########################


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        lefthalf = merge_sort(lefthalf)
        righthalf = merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

    return alist


# Detaillierte Erklärung: https://www.geeksforgeeks.org/merge-sort/
def merge_sort_log(alist, log=True):
    if len(alist) > 1:  # nur sortieren wenn |alist| > 1 ansonsten return alist
        mid = (
            len(alist) // 2
        )  # ganzzahlige Mitte der Liste bestimmen mit // (Dezimalstellen fallen weg, es wird auf nächstkleinere Ganzzahl gerundet)
        lefthalf = alist[:mid]  # Slicing
        righthalf = alist[mid:]

        lefthalf = merge_sort_log(lefthalf, log)  # rekursiver Aufruf
        righthalf = merge_sort_log(righthalf, log)  # rekursiver Aufruf

        i = 0  # Indice für linke Hälfte (definiert wo bereits sortiert wurde)
        j = 0  # Indice für rechte Hälfte (definiert wo bereits sortiert wurde)
        k = 0  # Indice für zusammengefügte Liste (wird laufend sortiert)

        while i < len(lefthalf) and j < len(righthalf):  # beide Hälften zusammenführen
            print("merging", lefthalf, righthalf, "with", i, j, k) if log else None
            if lefthalf[i] <= righthalf[j]:  # Elemente aus Hälften vergleichen
                alist[k] = lefthalf[
                    i
                ]  # wenn links kleiner gleich rechts zur sortieren Liste hinzufügen
                i += 1
            else:
                alist[k] = righthalf[
                    j
                ]  # wenn rechts kleiner als links zur sortierten Liste hinzufügen
                j += 1
            k += 1

        while i < len(lefthalf):  # in linker Hälfte verbleibende Elemente hinzufügen
            (
                print("remaining elements lefthalf", lefthalf, "with", i, j, k)
                if log
                else None
            )
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):  # in rechter Hälfte verbleibende Elemente hinzufügen
            (
                print("remaining elements righthalf", righthalf, "with", i, j, k)
                if log
                else None
            )
            alist[k] = righthalf[j]
            j += 1
            k += 1

    print("***") if log else None
    print(alist) if log else None
    print("***") if log else None

    return alist


# Anwendung

alist = [8, 3, 1, 5, 6, 2, 4, 7]
print(merge_sort_log(alist))
print(merge_sort(alist))

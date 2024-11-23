def bubble_sort_asc(num_list):
    n = len(num_list)
    
    # Repräsentiert jeden vollständigen Listendurchlauf
    for i in range(0, n):

        # Listendurchlauf von Index 0 bis zum kleinsten unsortierten Element n-i-1
        for j in range(0, n-i-1):            

            # Element mit nächst grösserem vergleichen und geg. austauschen
            if num_list[j] > num_list[j+1]:  
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    return num_list                    

def bubble_sort_desc(num_list):
    n = len(num_list)
    
    for i in range(0, n):
        for j in range(0, n-i-1):

            if num_list[j] < num_list[j+1]:  # einziger Unterschied zu bubble_sort_asc
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    return num_list


unsorted_list = [64, 34, 25, 12]             # Unsortierte numerische Liste
print(bubble_sort_asc(unsorted_list))        # >>> [11, 12, 22, 25, 34, 64, 90]

print(bubble_sort_desc(unsorted_list))       # >>> [90, 64, 34, 25, 22, 12, 11]


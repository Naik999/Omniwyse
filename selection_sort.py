my_list = input("enter")
my_list = [int(s)for s in my_list.split()]

def selection_sort(tap):   
    for i in range(len(tap)):
        min_val = i 
        for j in range(i + 1, len(tap)):
            if tap[j] < tap[min_val]:
                min_val = j 
        tap[i], tap[min_val] = tap[min_val], tap[i] 
selection_sort(my_list)
print("Sorted array:", my_list)

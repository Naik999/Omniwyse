num_a = input("give values with space: ")
num_a = [int(x) for x in  num_a.split()]

def bubble_number(a):  
    length_of = len(a)
    for i in range(length_of):
        for j in range(0,length_of-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
sorted_number = bubble_number(num_a)
print(sorted_number)

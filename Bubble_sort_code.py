def number():
    num = (input("enter:"))
    num = list(num)
    length_of = len(num)
    for i in range(length_of):
         for j in range(length_of):
                if num[i] < num[j]:
                    num[i],num[j] = num[j],num[i]
    return num
sorted_num = number()
print(sorted_num)

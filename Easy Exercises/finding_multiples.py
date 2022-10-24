# Finding the multiples of two given integers, e.g. 3 and 5, within a given range.

n = int(input("Add a number: "))
list = []

for i in range(n):
    if i % 3 == 0:
        list.append(i)
    elif i % 5 == 0:        # Making sure that there are no duplicates in the list
        list.append(i)

sum_of_list = sum(list)

print(sum_of_list)
print(list)

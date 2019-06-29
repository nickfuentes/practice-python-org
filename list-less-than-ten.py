array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_array = []

"""
for num in range(0, len(array), 1):
    if array[num] < 5:
        print(array[num])"""

# print(array[num]) print out numbers in arrary.


"""def less_than_5():
    for num in range(0, len(array), 1):
        if array[num] < 5:
            print(array[num])


less_than_5()"""


def less_than_5():
    for num in range(0, len(array), 1):
        if array[num] < 5:
            new_array.append(array[num])


# def print_new_array():
    for num in range(0, len(new_array), 1):
        print(new_array[num])


less_than_5()
print(new_array)
# print_new_array()

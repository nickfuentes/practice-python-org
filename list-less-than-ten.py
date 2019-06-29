array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""
for num in range(0, len(array), 1):
    if array[num] < 5:
        print(array[num])"""

# print(array[num]) print out numbers in arrary.


def less_than_5():
    for num in range(0, len(array), 1):
        if array[num] < 5:
            print(array[num])


less_than_5()

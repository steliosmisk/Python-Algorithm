def linear_search(my_list, value):
    for i in range(len(my_list)):
        if my_list[i] == value:
            print(f"Linear Search: Found {value} at index {i}")
            return i
    print(f"Not found {value}")
    return -1


def binary_search(my_list, value):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == value:
            print(f"Binary Search: Found {value} at index {mid}")
            return mid
        elif my_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Not found {value}")
    return -1


def bubble_sort(my_list):
    length = len(my_list)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print("Sorted:", my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, -3]
    print("List:", my_list)
    linear_search(my_list, 5)
    binary_search(my_list, 2)
    bubble_sort(my_list)

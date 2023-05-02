import time

def linear_search(my_list, value):
    start_time = time.time()
    for i in range(len(my_list)):
        if my_list[i] == value:
            print(f"Linear Search: Found {value} at index {i}")
            end_time = time.time()
            print(f"Time taken: {float(end_time - start_time)} seconds")
            return i
    print(f"Not found {value}")
    end_time = time.time()
    print(f"Time taken: {float(end_time - start_time)} seconds")
    return -1

def linear_search2(my_list, value):
    start_time = time.time()
    position = -1
    length = len(my_list) - 1
    while position < length:
        if my_list[position] == value:
            print(f"Linear Search (While method): Found {value} at index {position}")
            end_time = time.time()
            print(f"Time taken: {float(end_time - start_time)} seconds")
            return position
        position += 1
    end_time = time.time()
    print(f"Time taken: {float(end_time - start_time)} seconds")
    return -1

def binary_search(my_list, value):
    start_time = time.time()
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == value:
            print(f"Binary Search: Found {value} at index {mid}")
            end_time = time.time()
            print(f"Time taken: {float(end_time - start_time)} seconds")
            return mid
        elif my_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Not found {value}")
    end_time = time.time()
    print(f"Time taken: {float(end_time - start_time)} seconds")
    return -1

def bubble_sort(my_list):
    start_time = time.time()
    length = len(my_list)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print("Sorted:", my_list)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, -3]
    print("List:", my_list)
    linear_search(my_list, 5)
    linear_search2(my_list, 3)
    binary_search(my_list, 2)
    bubble_sort(my_list)

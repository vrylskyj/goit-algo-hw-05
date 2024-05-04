def binary_search(sorted_array, target):
    left = 0
    right = len(sorted_array) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if sorted_array[mid] == target:
            return iterations, sorted_array[mid]
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left < len(sorted_array):
        upper_bound = sorted_array[left]
    else:
        upper_bound = None

    return iterations, upper_bound

# Приклад використання:
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]
target = 6.6
iterations, upper_bound = binary_search(sorted_array, target)
print("Iterations:", iterations)
print("Upper Bound:", upper_bound)

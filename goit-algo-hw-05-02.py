def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None

    while low <= high:
        mid = (high + low) // 2
        iterations += 1

        # Порівнюємо значення посередині з x
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid] if upper_bound is None or arr[mid] < upper_bound else upper_bound
        else:
            upper_bound = arr[mid]
            return iterations, mid, upper_bound

    return iterations, -1, upper_bound

arr = [2.1, 3.5, 4.8, 10.2, 40.7]
x = 10.2
iterations, result, upper_bound = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result} with {iterations} iterations")
    print(f"Upper bound is {upper_bound}")
else:
    print(f"Element is not present in array with {iterations} iterations")
    print(f"Upper bound is {upper_bound}")
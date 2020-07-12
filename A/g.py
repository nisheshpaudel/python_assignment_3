def interpolationSearch(arr, n, x):
    L = 0
    R = (n - 1)

    while L <= R and x >= arr[L] and x <= arr[R]:
        if L == R:
            if arr[L] == x:
                return L
            return -1

        pos = L + int(((float(R - L) /
                         (arr[R] - arr[L])) * (x - arr[L])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            L = pos + 1

        else:
            R = pos - 1

    return -1

arr = [7, 9, 13, 15, 17, 19, 20, 22, 23, 26, 33, 35, 39, 44]

index = interpolationSearch(arr, len(arr), 23)

if index != -1:
    print(f"Element found at {index}")
else:
    print("Element not found")
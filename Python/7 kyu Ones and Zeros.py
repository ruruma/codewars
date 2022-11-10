def binary_array_to_number(arr):
    print(int("".join(map(str, arr)), 4))
    return int("".join(map(str, arr)), 2)


print(binary_array_to_number([1, 1, 1, 1]))

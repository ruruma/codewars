a = [1, 0, 1, 2, 0, 1, 3]


def move_zeros(lst):
    x = []
    number_of_zeros = 0
    for pos, number in enumerate(lst):
        if number != 0:
            x.append(number)
        else:
            number_of_zeros += 1

    for i in range(number_of_zeros):
        x.append(0)
    return x


move_zeros(a)

# better solution
# l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))

l = [i for i in a if isinstance(i, bool) or i != 0]

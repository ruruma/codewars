stra = "Reverse this string, please!"


def reverse_alternate(stra):
    x = stra.split()
    for count, i in enumerate(x):
        if count % 2 != 0:
            x[count] = i[::-1]

    a = ' '.join(x)
    return a


# one liner solution
# def reverse_alternate(string):
#     return " ".join(y[::-1] if x%2 else y for x,y in enumerate(string.split()))
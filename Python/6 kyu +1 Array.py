def up_array(arr):
    x = ''
    res = []
    for i in arr:
        x += str(i)

    result = int(x) + 1
    for i in str(result):
        res.append(i)
    return result


x = [1, 2, 3]

up_array(x)

def delete_nth(order, max_e):
    x = []

    for i in order:
        if x.count(i) < max_e:
            x.append(i)
    return x
def queue_time(cus, n):
    print(cus, n)
    tills = [0] * n
    for i in cus:
        tills[0] += i
        tills.sort()
    return max(tills)

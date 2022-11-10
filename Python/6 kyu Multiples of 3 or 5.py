def solution(number):
    sum_i = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_i += i

    return sum_i
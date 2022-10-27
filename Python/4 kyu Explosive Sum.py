def exp_sum(n):
    if n < 0:
        return 0
    dp = [1] + [0] * n
    for num in range(1, n + 1):
        print(num)
        for i in range(num, n + 1):
            print("*"*30 + " printing i")
            print(i)
            print("*" * 30 + " finished i")
            dp[i] += dp[i - num]
    return dp[-1]


print(exp_sum(5))

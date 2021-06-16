stp = 1

# def golomb(n):
#     global stp
#     print(stp)
#     stp += 1
#     if n == 1:
#         return 1
#     return 1 + golomb(n - golomb(golomb(n - 1)))

def golombMemo(n, memo={}):
    global stp
    print(stp)
    stp += 1
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + golombMemo(n - golombMemo(golombMemo(n - 1)))

    return memo[n]

# def golombButtomUp(n):
#     global stp
    
#     if n == 1:
#         return 1

#     # if n not in memo:
#     #     memo[n] = 1 + golombMemo(n - golombMemo(golombMemo(n - 1)))
#     g = 0
#     for d in range(2, n):
#         g += (1 + (n - (n - 1)))

#     return g

# print(golombButtomUp(10))

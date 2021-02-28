@njit(cache=True)
def comb(n, k):
    n = int(n)
    k = int(k)
    if (k > n) or (n < 0) or (k < 0):
        return 0
    val = 1
    for j in range(min(k, n - k)):
        val = (val * (n - j)) // (j + 1)
    return val

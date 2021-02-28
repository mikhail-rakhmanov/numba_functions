@njit(cache=True)
def combinations(n, k):
    a = np.ones((k, n - k + 1), dtype=np.int64)
    a[0] = np.arange(n - k + 1)
    for j in range(1, k):
        reps = (n - k + j) - a[j - 1]
        size = np.sum(reps)
        n_a = np.empty((k, size), dtype=np.int64)
        for m in range(k):
            n_a[m] = np.repeat(a[m, :], reps)

        a = n_a
        ind = np.cumsum(reps)
        for p, q in np.nditer((ind[:-1], reps[1:])):
            a[j, p] = 1 - q

        a[j, 0] = j
        a[j] = np.cumsum(a[j])

    return a

def f(v,n):
    if n == 0:
        return 0
    else:
        s = f(v, n-1)
        if (v[n-1] > 0):
            s = s + v[n-1]
        return s
    
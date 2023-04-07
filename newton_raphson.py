def newton_raphson(f, df, x0, tol=1.0e-09, maxIter=100):
    xk = x0
    for k in range(maxIter):
        xkp1 = xk - 1*f(xk)/df(xk)
        error = (xkp1 - xk)
        if abs(error) < tol:
            break
        xk = xkp1
    return xkp1, k
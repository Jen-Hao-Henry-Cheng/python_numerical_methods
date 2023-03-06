def newton_raphson(f, df, x0, tol=1.0e-09, maxIter=100):
    xk = x0
    for k in range(maxIter):
        xkp1 = xk - 1*f(xk)/df(xk)
        error = (xkp1 - xk)
        if abs(error) < tol:
            return xkp1, k
        xk = xkp1
        print(f'k = {k+1}, {xk=}, {error=}')
    print('Too many iteration\n')
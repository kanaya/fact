def fact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 1
    return r

def fact_r(n):
    if n == 0:
        return 1
    else:
        return n * fact_r(n-1)

f = fact(100)
f_r = fact_r(100)
print("{} and {}".format(f, f_r))


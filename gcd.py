m = 15
n = 14
if(m % n == 0):
    (m, n) = (n, m % n)
else:
    gcd = n

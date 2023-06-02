def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def reverse(n):
    n = int(str(n)[::-1])
    return n


def isEmirp(n):
    if isPrime(n) and reverse(n) != n and isPrime(reverse(n)):
        return True
    return False


c = 0
for i in range(10, 2 ** 100):
    if isEmirp(i):
        c += 1
        print('%5d' % i, end=' ')
        if c % 10 == 0:
            print('')
    if c == 100:
        break

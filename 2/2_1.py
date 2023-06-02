def sqrt(n):
    lastGuess = n
    while True:
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        if abs(nextGuess - lastGuess) >= 0.0001:
            lastGuess = nextGuess
        elif abs(nextGuess - lastGuess) < 0.0001:
            return nextGuess


while True:
    try:
        n = float(input('Please enter a positive number:'))
        if n >= 0:
            print('The approximation of its square root is %f' % sqrt(n))
            break
        else:
            print('The number should be positive!')
    except:
        print('The input must be a positive number!')

while True:
    N = input('Please enter a positive integer:')
    try:
        N = int(N)
        if N > 2:
            count = 0
            for digit in range(2, N):
                flag = True
                for i in range(2, digit):
                    if digit % i == 0:
                        flag = False
                        break
                if flag:
                        print(digit,end=' ')
                        count+=1
                        if count % 8 == 0:
                            print('')
            break
        elif N == 1 or N ==2:
            print('No primes smaller than %s.'%N)
            continue
        else:
            print('You must enter a positive integer!')
            continue
    except:
        print('You must enter a positive integer!')
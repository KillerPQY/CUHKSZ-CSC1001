while True:
    N = input('Please enter a positive integer:')
    try:
        N = int(N)
        if N >0:
            print("\tm\tm+1\tm**(m+1)")
            for i in range(1,N+1):
                print("\t%d\t%d\t%d"%(i,i+1,i**(i+1)))
            break
        else:
            print('Please enter a positive integer!')
            continue
    except:
        print('Please enter a positive integer!')
        continue
from math import sin, cos, tan
while True:
    f = input('Please enter a trigonometric function(sin,cos,tan):')
    try:
        eval(f+"(5)")
        break
    except:
        print('The input should be one of\"sin\", \"cos\", \"tan\"!')
while True:
    a = input('Please enter the interval initial point:')
    try:
        a=float(a)
        break
    except:
        print('\"a\" should be a number!')
while True:
    b = input('Please enter the interval end point:')
    try:
        b = float(b)
        break
    except:
        print('\"b\" should be a number!')
while True:
    n = input('Please enter a positive integer:')
    try:
        n = int(n)
        if n > 0:
            result = 0
            for i in range(1,n+1):
                mid = eval('((b-a)/n)*'+f+'(a+((b-a)/n)*(i-1/2))')
                result = result + mid
            print('The result of that equation is %s.'%result)
            break
        else:
            print('\"n\" should be a positive integer!')
            continue
    except:
            print('\"n\" should be a positive integer!')    
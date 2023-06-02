def hanoiOriginalStack3(n, a, b, c):
    stack = []
    while n > 0 or len(stack) > 0:
        while n > 0:
            paramsRight = [False, n-1, b, a, c]
            stack.append(paramsRight)
            n -= 1
            c, b = b, c
        finishRight = stack.pop()
        if not finishRight[0]:
            print("move %s from %s to %s" % (finishRight[1]+1, finishRight[3], finishRight[4]))
            finishRight[0] = True
            n, b, a, c = finishRight[1:]
            a, b, c = b, a, c
            if n > 0:
                stack.append(finishRight)
hanoiOriginalStack3(3, "a", "b", "c")
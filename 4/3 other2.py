def hanoiStack(n, a, b, c):
    stack = []
    while n > 0 or len(stack) > 0:
        while n > 0:
            paramsLeft = [True, n-1, a, c, b]
            paramsRight = [False, n-1, b, a, c]
            stack.append(paramsRight)
            stack.append(paramsLeft)
            n -= 1
            c, b = b, c
        finishLeft = stack.pop()
        finishRight = stack.pop()
        if not finishRight[0]:
            # 如果子问题3是False,先解决子问题2，再把子问题3转为它自己的子问题，False改为True.
            print("move %s from %s to %s" % (finishRight[1]+1, finishRight[3], finishRight[4]))
            finishRight[0] = True
            n, b, a, c = finishRight[1:]
            a, b, c = b, a, c
            if n > 0:
                stack.append(finishRight)
                stack.append(finishLeft)
hanoiStack(2, "a", "b", "c")
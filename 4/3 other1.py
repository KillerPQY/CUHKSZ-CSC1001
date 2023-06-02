def hanoiStack(n, a, b, c):
    stack = []
    while n > 0 or len(stack)>0:
        while n > 0:
            # 问题(n,a,b,c)可以转为3个子问题，1汉诺塔(n-1,a,c,b)，2移动(打印)(n,a,c)和3汉诺塔(n-1,b,a,c)
            # 压入子问题1的三个子问题，子问题1的解决转化为三个新的子问题，相当于子问题1已经解决了，所以用True来表示，False表示子问题未解决。
            params = [[True, n-1, a, c, b], [False, n, a, c], [False, n-1, b, a, c]]
            stack.append(params)
            n -= 1
            a, b, c = a, c, b
        finish = stack.pop()
        if not finish[1][0]:
            print("%s --> %s" % (finish[1][2], finish[1][3]))
            finish[1][0] = True
        if not finish[2][0]:
            n = finish[2][1]
            finish[2][0] = True
            if n > 0:
                stack.append(finish)
                a, b, c = finish[2][2:]
hanoiStack(2, "a", "b", "c")
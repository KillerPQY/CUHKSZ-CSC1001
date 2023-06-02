def InitializeLockers():
    n = 0
    l = []
    while n < 100:
        l.append(False)
        n += 1
    return l


def studentChange(l: list, n: int):
    for i in range(1, len(l) + 1):
        if i % n == 0:
            if l[i - 1] == False:
                l[i - 1] = True
            else:
                l[i - 1] = False
    return l


l1 = InitializeLockers()
for i in range(1, 101):
    l1 = studentChange(l1, i)
x = 0
y = 0
open = []
for i, j in enumerate(l1):
    if j == True:
        x += 1
        open.append(str(i+1))
    else:
        y += 1
print('%d lockers are open, %d lockers are closed.' % (x, y))
print(", ".join(open) + 'lockers are open.')
import random


def judge(pos, nextcolumn):
    nextrow = len(pos)
    for i in range(nextrow):
        if abs(pos[i] - nextcolumn) in (0, nextrow - i):
            return False
    return True


def queens(num=8, pos=[]):
    if num - 1 == len(pos):
        for nextcolumn in range(num):
            if judge(pos, nextcolumn):
                yield [nextcolumn]
    else:
        for nextcolumn in range(num):
            if judge(pos, nextcolumn):
                for result in queens(num, pos + [nextcolumn]):
                    yield [nextcolumn] + result


def displaytable(l):
    length = len(l)
    for column in l:
        print('| ' * column + '|Q' + '| ' * (length - column - 1) + '|')

print(list(queens(8)))
displaytable(random.choice(list(queens(8))))

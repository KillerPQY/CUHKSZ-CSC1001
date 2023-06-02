class Stack():
    def __init__(self):
        self.data = list()

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            print('The stack is empty.')
        else:
            return self.data[len(self.data) - 1]

    def pop(self):
        if self.is_empty():
            print('The stack is empty.')
        else:
            return self.data.pop()

    def __len__(self):
        return len(self.data)


def HanoiTower(n):
    questions = Stack()
    a, b, c = "A", "B", "C"
    # 问题(n,a,b,c)可以转为3个子问题，1. HanoiTower(n-1,a,c,b), 2. 移动(打印)(n,a,c), 3. HanoiTower(n-1,b,a,c)
    while n > 0 or len(questions)>0:
        while n > 0:
            subquestions = [[True, n-1, a, c, b], [False, n, a, c], [False, n-1, b, a, c]]
            questions.push(subquestions)
            n -= 1
            a, b, c = a, c, b
        q = questions.pop()
        if not q[1][0]:
            print("%s --> %s" % (q[1][2], q[1][3]))
            q[1][0] = True
        if not q[2][0]:
            n = q[2][1]
            q[2][0] = True
            if n > 0:
                questions.push(q)
                a, b, c = q[2][2:]

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Please enter the number of disks: "))
            if n > 0:
                break
            else:
                print("The number of disks should be positive!")
        except ValueError:
            print('The input should be a positive integer!')
    HanoiTower(n)
    
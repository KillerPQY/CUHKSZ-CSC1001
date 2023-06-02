class Polynomial:
    def __init__(self, poly=None):
        self.poly = poly

    def first_diff(self):
        poly = self.poly.replace('-', '+-')
        for i in poly:
            if i.isalpha():
                x = i
                break
        answer = ""
        l = poly.split('+')
        for i in l:
            x_pos = i.find(x)
            if i[:x_pos] == "":
                i = "1*" + i
            elif i[:x_pos] == "-":
                i = i[:x_pos] + "1*" + i[x_pos:]
            x_pos = i.find(x)
            if i.find("^") == -1:
                if x_pos == -1:
                    pass
                else:
                    answer = answer + "+" + i[:x_pos - 1]
            else:
                try:
                    n = int(i[i.find("^") + 1:])
                    c = int(i[:x_pos - 1])
                except BaseException:
                    n = float(i[i.find("^") + 1:])
                    c = float(i[:x_pos - 1])
                c = c * n
                n = n - 1
                if n != 1:
                    answer = answer + "+" + str(c) + "*" + x + "^" + str(n)
                else:
                    answer = answer + "+" + str(c) + "*" + x
        answer = answer.replace('+-', '-')
        answer = answer.replace('1*', '')
        answer = answer.lstrip("+")
        return answer


def main():
    x = Polynomial(input('Please enter a polynomial:'))
    print('The first derivative of the polynomial is %s' % x.first_diff())


if __name__ == '__main__':
    main()

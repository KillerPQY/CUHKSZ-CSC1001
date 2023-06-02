def sumOfDoubleEvenPlace(number):
    s1 = str(number)
    sum = 0
    for i in range(len(s1) - 2, -1, -2):
        sum += getDigit(int(s1[i]) * 2)
    return sum


def getDigit(number):
    s1 = str(number)
    if len(s1) == 1:
        return int(s1)
    elif len(s1) == 2:
        sum = int(s1[0]) + int(s1[1])
        return sum


def sumOfOddPlace(number):
    s1 = str(number)
    sum = 0
    for i in range(len(s1) - 1, -1, -2):
        sum += int(s1[i])
    return sum


def isValid(number):
    if len(str(number)) <= 16 and len(str(number)) >= 13:
        if str(number).startswith('4') or str(number).startswith('5') or str(
                number).startswith('37') or str(number).startswith('6'):
            oddsum = sumOfOddPlace(number)
            evensum = sumOfDoubleEvenPlace(number)
            sum = oddsum + evensum
            if sum % 10 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


while True:
    num = input('Please enter a credit card number as an integer:')
    try:
        num = int(num)
        if num > 0:
            if isValid(num):
                print('The number is valid.')
            else:
                print('The number is invalid')
            break
        else:
            print('You should enter a credit card number as an integer!')
    except:
        print('You should enter a credit card number as an integer!')

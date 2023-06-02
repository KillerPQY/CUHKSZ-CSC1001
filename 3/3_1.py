class Flower:
    def __init__(self, name=None, petals=None, price=None):
        self.name = str(name)
        self.petals = int(petals)
        self.price = float(price)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = str(name)

    def get_petals(self):
        return self.petals

    def set_petals(self, petals):
        self.petals = int(petals)


    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = float(price)


def main():
    name = input('Please enter flower\'s name:')
    while True:
        try:
            petals = int(input('Please enter number of petals:'))
            break
        except ValueError:
            print('Petals should be an integer!')
    while True:
        try:
            price = float(input('Please enter flower\' price:'))
            break
        except ValueError:
            print('Price should be a float!')
    f = Flower(name, petals, price)
    print('Name: %s Petals: %d Price: %f' % (f.get_name(), f.get_petals(), f.get_price()))
    new_name = input('Please enter new name:')
    f.set_name(new_name)
    while True:
        try:
            new_petals = input('Please enter new petals number:')
            f.set_petals(new_petals)
            break
        except ValueError:
            print('Petals should be an integer!')
    while True:
        try:
            new_price = input('Please enter new price:')
            f.set_price(new_price)
            break
        except ValueError:
            print('Price should be a float!')
    print('Name: %s Petals: %d Price: %f' % (f.get_name(), f.get_petals(), f.get_price()))


if __name__ == '__main__':
    main()
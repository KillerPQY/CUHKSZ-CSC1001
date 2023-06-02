import random


class Ecosystem:
    def __init__(self, length=0, fishes=0, bears=0):
        self.length = length
        self.fishes = fishes
        self.bears = bears
        self.river = []
        for i in range(self.fishes):
            self.river.append('F')
        for i in range(self.bears):
            self.river.append('B')
        for i in range(self.length - self.fishes - self.bears):
            self.river.append('N')
        random.shuffle(self.river)

    def same_animal_collide(self, animal):
        if 'N' in self.river:
            l = list(index for (index, value) in enumerate(self.river) if value == 'N')
            self.river[random.choice(l)] = animal

    def bear_fish_collide(self, bear, fish):
        self.river[bear] = 'B'
        self.river[fish] = 'N'

    def no_collide(self, pos, move):
        self.river[pos], self.river[pos + move] = self.river[pos + move], self.river[pos]

    def simulation(self, steps):
        canMove = [1, -1, 0]
        for i in range(steps):
            for j in range(self.length):
                if self.river[j] != "N":
                    move = random.choice(canMove)
                    if move == 0:
                        pass
                    elif move == 1 and j < (self.length - 1):
                        if self.river[j] == self.river[j + 1]:
                            self.same_animal_collide(self.river[j])
                        elif self.river[j + 1] == 'N':
                            self.no_collide(j, move)
                        elif self.river[j] == 'B' and self.river[j + 1] == 'F':
                            self.bear_fish_collide(j, j + 1)
                        elif self.river[j] == 'F' and self.river[j + 1] == 'B':
                            self.bear_fish_collide(j + 1, j)
                    elif move == -1 and j > 0:
                        if self.river[j] == self.river[j - 1]:
                            self.same_animal_collide(self.river[j])
                        elif self.river[j - 1] == 'N':
                            self.no_collide(j, move)
                        elif self.river[j] == 'B' and self.river[j - 1] == 'F':
                            self.bear_fish_collide(j, j - 1)
                        elif self.river[j] == 'F' and self.river[j - 1] == 'B':
                            self.bear_fish_collide(j - 1, j)
    def show_river(self):
        return self.river


def main():
    flag = True
    while flag:
        while True:
            try:
                l = int(input('Please enter the river length:'))
                break
            except ValueError:
                print('You should enter an integer.')
        while True:
            try:
                f = int(input('Please enter the number of fishes:'))
                break
            except ValueError:
                print('You should enter an integer.')
        while True:
            try:
                b = int(input('Please enter the number of bears:'))
                break
            except ValueError:
                print('You should enter an integer.')
        if f + b <= l:
            flag = False
        else:
            print('The number of fishes plus the number of bears should smaller than or equal to the river length.')
            print('Please enter all numbers again!')
    e = Ecosystem(l, f, b)
    print(e.show_river())
    while True:
        try:
            s = int(input('Please enter the simulation times:'))
            e.simulation(s)
            print(e.show_river())
            break
        except ValueError:
            print('The simulation times should be an integer! Enter again!')


if __name__ == '__main__':
    main()

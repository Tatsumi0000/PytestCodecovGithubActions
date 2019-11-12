class Sample:

    def __init__(self):
        self.x = self.y = 0

    def add(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y

    def sub(self, x, y):
        self.x = x
        self.y = y
        return self.x - self.y


if __name__ == '__main__':
    sample = Sample()
    print('{0}'.format(sample.add(x=0, y=1)))

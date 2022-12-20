class Car:

    x = 'ABC'

    def __init__(self, name, year, color):
        self.year = year
        self.color = color
        self.name = name

    def drive(self):
        print('%s started', self.name)

    @staticmethod
    def hello():
        print('Hello')

    @classmethod
    def show(cls):
        print(cls.x)
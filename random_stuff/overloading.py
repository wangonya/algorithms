class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        """by defaul the + operator is undefined for new classes
        unless we define this, python won't know how to x+y"""
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        """again, str is undefined. we need to tell python how to display
        the result - otherwise we get <__main__.Point object at 0x...>"""
        return f'{self.x},{self.y}'


if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(-1, 2)
    # __add__ needs to be explicitly defined in Point for this to work
    sum_ = p1 + p2
    print(f'sum = {sum_}')

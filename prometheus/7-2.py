class Ball:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'Ball'

    def __repr__(self):
        return f'Ball("{self.color}")'


test = Ball('red')
test1 = Ball("red")

print(test1)

# print(repr(test1))
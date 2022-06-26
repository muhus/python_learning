def add_five(x, y, z):
    return x + 5


def do_twice(f):
    print(f)
    def resulting_func(x):  #звідки висрався йобаний ікс?
        return f(f(x))

    return resulting_func


wtf = do_twice(add_five)

print(wtf(5,10,20))

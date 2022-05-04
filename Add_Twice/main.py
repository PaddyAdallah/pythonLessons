if __name__ == "main":

    def apply_twice(func, arg):
        return func(func(arg))

    def add_five(x):
        return x + 5

    print(apply_twice(add_five, 10))
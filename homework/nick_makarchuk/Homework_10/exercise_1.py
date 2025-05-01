def finish_me(func):
    def wrapper():
        func()
        print("finished")
    return wrapper


@finish_me
def hello_world():
    print("Hello, world!")


hello_world()

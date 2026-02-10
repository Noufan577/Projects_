import time

def decorator(fucntion):
    def wrapper():
        time.sleep(2)
        fucntion()
    return wrapper

@decorator
def say_hello():
    print("hello")
def say_Bye():
    print("Bye")

say_hello()
say_Bye()


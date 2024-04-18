def print_something():
    print('Print something')


def sum(a, b):
    print(a + b)


#print_something()
#sum(1, 2)


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


#parent()


def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper

#decorator_variable = my_decorator(print_something)
#decorator_variable()

@my_decorator
def print_something_wuth_decorator():
    print("print_something")


print_something_wuth_decorator()
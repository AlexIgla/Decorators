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


#print_something_wuth_decorator()



from decorators import do_twice

@do_twice
def test_twice_without_params():
    print("Этот вызов без параметров")


@do_twice
def test_twice_2_params(str1, str2):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))

test_twice_without_params()
test_twice_2_params("1", "2")
test_twice("single")

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

decorated_value = test_twice("single")
print(decorated_value)


@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

print(test_twice.__name__)



def debug(func):
    """Выводит сигнатуру функции и возвращаемое значение"""
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} вернула значение - {value!r}")
        return value
    return wrapper_debug


@debug
def age_passed(name, age=None):
  if age is None:
    return "Необходимо передать значение age"
  else:
    return "Аргументы по умолчанию заданы!"

age_passed("Роман")
age_passed("Роман", age=21)
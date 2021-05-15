from functools import wraps


def force_arg_type(required_type):
    def decorator(func):
        @wraps(func)
        def inner(*args):
            if not all([isinstance(arg, required_type) for arg in args]):
                raise ValueError(
                    f"Все аргументы должны быть {required_type.__name__}"
                )
            return func(*args)
        return inner
    return decorator


force_type = {
    "numbers": force_arg_type(int),
    "strings": force_arg_type(str),
}


@force_type["numbers"]
def summ(a, b):
    return a + b


if __name__ == "__main__":
    summ(1, 2)
    # summ("2", "2")

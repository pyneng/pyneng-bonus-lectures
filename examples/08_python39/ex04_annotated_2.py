# source https://stackoverflow.com/questions/66451253/is-there-a-way-to-specify-a-range-of-valid-values-for-a-function-argument-with-t

import inspect


@dataclass
class ValueRange:
    min: float
    max: float

    def validate_value(self, x):
        if not (self.min <= x <= self.max):
            raise ValueError(f"{x} must be in range [{self.min}, {self.max}]")


def check_annotated(func):
    hints = get_type_hints(func, include_extras=True)
    spec = inspect.getfullargspec(func)

    def wrapper(*args, **kwargs):
        for idx, arg_name in enumerate(spec[0]):
            hint = hints.get(arg_name)
            validators = getattr(hint, "__metadata__", None)
            if not validators:
                continue
            for validator in validators:
                validator.validate_value(args[idx])

        return func(*args, **kwargs)

    return wrapper


@check_annotated
def function_2(
    number: Union[float, int], fraction: Annotated[float, ValueRange(0.0, 1.0)] = 0.5
):
    return fraction * number


"""
In [92]: function_2(1, 2)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-92-c9345023c025> in <module>
----> 1 function_2(1, 2)

<ipython-input-90-01115cb628ba> in wrapper(*args, **kwargs)
     10                 continue
     11             for validator in validators:
---> 12                 validator.validate_value(args[idx])
     13
     14         return func(*args, **kwargs)

<ipython-input-87-7f4ac07379f9> in validate_value(self, x)
      6     def validate_value(self, x):
      7         if not (self.min <= x <= self.max):
----> 8             raise ValueError(f'{x} must be in range [{self.min}, {self.max}]')
      9

ValueError: 2 must be in range [0.0, 1.0]

In [93]: function_2(1, 1)
Out[93]: 1
"""

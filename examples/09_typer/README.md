## Typer

* [Typer github](https://github.com/tiangolo/typer)
* [Typer docs](https://typer.tiangolo.com/tutorial/)
* [Typer cli](https://typer.tiangolo.com/typer-cli/)
* [Type annotations cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)


New topics:

* [Enum docs](https://docs.python.org/3/library/enum.html), [enum stackoverflow](https://stackoverflow.com/questions/37601644/python-whats-the-enum-type-good-for)


## notes

Argument

```python
def main(ip_address: str, count: int = typer.Argument(...)):
def main(ip_address: str, count: Optional[int] = typer.Argument(3)):
def main(ip_address: str, count: Optional[int] = typer.Argument(None)):
```

from typing import Tuple
import typer


def cli1(user_params: Tuple[str, str, int]):
    """
    Функция создает пользователя с параметрами
    USER_PARAMS: username, password, level
    """
    print(user_params)


def cli2(
    username: str,
    password: str = typer.Option(
        ..., prompt=True, hide_input=True, confirmation_prompt=True
    ),
    level: int = 5,
):
    """
    Функция создает пользователя с параметрами: username, password, level
    """
    print(f"{username=} {password=} {level=}")


if __name__ == "__main__":
    typer.run(cli2)

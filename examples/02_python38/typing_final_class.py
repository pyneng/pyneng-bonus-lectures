from typing import Final


class BaseSSH:
    TIMEOUT: Final[int] = 10


class CiscoSSH(BaseSSH):
    TIMEOUT = 1

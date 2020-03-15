from typing import final


class BaseSSH:
    @final
    def done(self) -> None:
        pass


class CiscoSSH(BaseSSH):
    def done(self) -> None:
        pass



@final
class CiscoIosSSH:
    pass


class Other(CiscoIosSSH):
    pass

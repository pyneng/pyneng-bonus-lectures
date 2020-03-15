from typing import Protocol
from netmiko import ConnectHandler


class ConnectSSH(Protocol):
    def send_command(self, command: str) -> str:
        ...

    def send_config_commands(self, commands: str) -> str:
        ...


class CiscoSSH:
    device_type = "cisco_ios"

    def __init__(self, ip, username, password, enable_password, disable_paging=True):
        self._ssh = ConnectHandler(
            device_type=self.device_type,
            host=ip,
            username=username,
            password=password,
            secret=enable_password,
        )

    def send_command(self, command: str) -> str:
        result = self._ssh.send_command(command)
        return result

    def send_config_commands(self, commands: str) -> str:
        result = self._ssh.send_config_set(commands)
        return result


def func(connection: ConnectSSH, command: str) -> str:
    return connection.send_command(command)


if __name__ == "__main__":
    r1 = CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco")
    print(func(r1, "sh clock"))

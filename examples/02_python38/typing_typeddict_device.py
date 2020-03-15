from netmiko import ConnectHandler
from typing import List, TypedDict, NamedTuple


class DeviceParams(TypedDict, total=False):
    device_type: str
    host: str
    username: str
    password: str
    secret: str
    port: int


def send_show(device_dict: DeviceParams, command: str) -> str:
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


if __name__ == "__main__":
    r1 = DeviceParams(
        device_type="cisco_ios",
        host="192.168.100.1",
        username="cisco",
        password="cisco",
        secret="cisco",
        port=20020,
    )
    print(send_show(r1, "sh clock"))

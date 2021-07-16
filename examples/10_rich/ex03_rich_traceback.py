from pprint import pprint
import netmiko
from rich.traceback import install
install()


def send_show(device, command):
    with netmiko.Netmiko(**device) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        return output


if __name__ == "__main__":
    r1 = {
        "device_type": "cisco_ios",
        "username": "cisco",
        "host": "192.168.100.11",
        "password": "cisco",
        "secret": "cisco",
        "timeout": 5,
    }
    send_show(r1, "sh clock")

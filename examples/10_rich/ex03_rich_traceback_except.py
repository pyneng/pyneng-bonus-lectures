from pprint import pprint
import netmiko
import paramiko
from rich.console import Console

console = Console()


def send_show(device, command):
    try:
        with netmiko.Netmiko(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            return output
    except netmiko.NetmikoTimeoutException as error:
        print(f"Failed to connect to {device['host']}")
        console.print_exception()
    except paramiko.ssh_exception.AuthenticationException:
        print(f"Authentication error on {device['host']}")
        console.print_exception()




if __name__ == "__main__":
    r1 = {
        "device_type": "cisco_ios",
        "username": "cisco",
        "host": "192.168.100.11",
        "password": "cisco",
        "secret": "cisco",
        "timeout": 5,
    }
    r2 = {
        "device_type": "cisco_ios",
        "username": "cisco",
        "host": "192.168.100.2",
        "password": "cisco",
        "secret": "cisco",
        "timeout": 5,
    }
    send_show(r1, "sh clock")
    send_show(r2, "sh clock")

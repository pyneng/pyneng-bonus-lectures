import subprocess
from pprint import pprint
from typing import List, Tuple
import typer


def ping_ip(ip_address, count):
    """
    Ping IP_ADDRESS and return True/False
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True
    else:
        return False


def main(ip_addresses: List[str], count: int = 3):
    """
    Ping IP_ADDRESS
    """
    # pprint(ip_addresses)
    for ip in ip_addresses:
        status = ping_ip(ip, count)
        if status:
            print(f"IP-адрес {ip:15} пингуется")
        else:
            print(f"IP-адрес {ip:15} не пингуется")


if __name__ == "__main__":
    typer.run(main)

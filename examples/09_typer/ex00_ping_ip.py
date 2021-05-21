import subprocess
from pprint import pprint
import typer
from typing import Optional


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


#def main(ip_address: str, count: int):
def main(ip_address: str, count: int = typer.Argument(...)):
def main(ip_address: str, count: Optional[int] = typer.Argument(3)):
def main(ip_address: str, count: Optional[int] = typer.Argument(None)):
    """
    Ping IP_ADDRESS
    """
    pprint(ip_address)
    pprint(count)
    status = ping_ip(ip_address, count)
    if status:
        print(f"IP-адрес {ip_address:15} пингуется")
    else:
        print(f"IP-адрес {ip_address:15} не пингуется")


if __name__ == "__main__":
    typer.run(main)

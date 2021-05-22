from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import repeat
import subprocess
from pprint import pprint
from typing import List, Tuple
import typer


def ping_ip(ip_address: str, count: int) -> bool:
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


def ping_ip_addresses(ip_addresses, count, limit=10):
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(ping_ip, ip_addresses, repeat(count))
        with typer.progressbar(length=len(ip_addresses)) as bar:
            for ip, status in zip(ip_addresses, results):
                if status:
                    reachable.append(ip)
                else:
                    unreachable.append(ip)
                bar.update(1)
    return reachable, unreachable


def cli(ip_addresses: List[str], count: int = 3):
    # print(f"{ip_addresses=}")
    # print(f"{count=}")
    ok, not_ok = ping_ip_addresses(ip_addresses, count)
    print("Пингуются")
    for ip in ok:
        typer.secho(ip, fg="green")
    print("Не пингуются")
    for ip in not_ok:
        typer.secho(ip, fg="red")


if __name__ == "__main__":
    typer.run(cli)

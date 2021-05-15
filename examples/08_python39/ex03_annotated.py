from platform import system as system_name
from typing import Annotated, get_type_hints
import subprocess
from concurrent.futures import ThreadPoolExecutor


IPAddress = Annotated[str, "IP address"]


def ping_ip(ip: IPAddress) -> bool:
    param = "-n" if system_name().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    reply = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ip_is_reachable = reply.returncode == 0
    return ip_is_reachable


def ping_ip_list(
    ip_list: list[IPAddress], limit: int = 3
) -> tuple[list[IPAddress], list[IPAddress]]:
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(ping_ip, ip_list)
    for ip, status in zip(ip_list, results):
        if status:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return reachable, unreachable


if __name__ == "__main__":
    print(get_type_hints(ping_ip, include_extras=True))

from platform import system as system_name
import subprocess
from concurrent.futures import ThreadPoolExecutor


def ping_ip(ip: str) -> bool:
    param = "-n" if system_name().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    reply = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ip_is_reachable = reply.returncode == 0
    return ip_is_reachable


def ping_ip_list(ip_list: list[str], limit: int = 3) -> tuple[list[str], list[str]]:
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


from typing import List, Tuple


def ping_ip_list_2(ip_list: List[str], limit: int = 3) -> Tuple[List[str], List[str]]:
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

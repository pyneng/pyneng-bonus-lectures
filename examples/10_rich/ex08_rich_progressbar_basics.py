import subprocess
from rich.progress import track


def ping_ip(ip_address, count):
    """
    Ping IP_ADDRESS and return True/False
    """
    print(f"Ping ip {ip_address}")
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


def ping_ip_addresses(ip_addresses, count):
    reachable = []
    unreachable = []
    for ip in track(ip_addresses, description="Пингую адреса"):
        if ping_ip(ip, count):
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return reachable, unreachable


if __name__ == "__main__":
    ip_list = ["8.8.8.8", "8.8.4.4", "192.168.100.1", "192.168.100.2", "192.168.100.3"]
    reachable, unreachable = ping_ip_addresses(ip_list, count=3)
    for ip in reachable:
        print(f"IP-адрес {ip:15} пингуется")
    for ip in unreachable:
        print(f"IP-адрес {ip:15} не пингуется")


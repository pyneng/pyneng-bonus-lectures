import subprocess
import click


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


@click.command()
@click.argument("ip_address")
@click.option("--count", "-c", default=2, type=int, help="Number of packets")
def main(ip_address, count):
    """
    Ping IP_ADDRESS
    """
    result = ping_ip(ip_address, count)
    print(result)


if __name__ == "__main__":
    main()


import time
import subprocess
from collections import Iterable


# Setup constants
mngmnt_screen = 0
slp_time = 0.5
alld = range(1, 8)
allr = range(1, 8)
# allsw = range(11,15)


traceroute = "traceroute {}"
traceroute_s = "traceroute {} source {}"


# Functions for TESTs
def show_command(r_id, cmd):
    send_commands(r_id, cmd, return_to_mngmt=False)


def ping(r_id, d_ip, s_ip=""):
    if s_ip:
        write_to(r_id, f"ping {d_ip} source {s_ip}")
    else:
        write_to(r_id, f"ping {d_ip}")


def trace(r_id, d_ip, s_ip=""):
    if s_ip:
        write_to(r_id, traceroute_s.format(d_ip, s_ip))
    else:
        write_to(r_id, traceroute.format(d_ip))


def send_commands(r_id, cmds, return_to_mngmt=False, fast=True):
    if type(r_id) == int:
        write_to(r_id, cmds, mngmnt_screen, return_to_mngmt, fast)
    elif isinstance(r_id, Iterable):
        for rid in r_id:
            write_to(rid, cmds, mngmnt_screen, return_to_mngmt, fast)


# Functions
def write_to(
    r_id, commands, return_to_screen=mngmnt_screen, return_to_mngmt=True, fast=False
):
    if type(commands) == str:
        commands = commands.splitlines()
    for line in commands:
        run(f"tmux select-window -t {r_id}")
        run(f'tmux send-keys -t {r_id} "{line}" Enter')
        if fast:
            time.sleep(slp_time)
        else:
            time.sleep(5)
    if return_to_mngmt:
        run(f"tmux select-window -t {return_to_screen}")


def run(line):
    subprocess.run(line, shell=True)


if __name__ == "__main__":
    from IPython import embed
    from traitlets.config import get_config
    c = get_config()
    c.InteractiveShellEmbed.colors = "Linux"
    embed(config=c)

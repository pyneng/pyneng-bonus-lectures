hardstatus on
defscrollback 10000
hardstatus alwayslastline
hardstatus string "%{rk}PyNEng%{bk}@%H %{gk}%c %{yk}%d.%m %{wk}%?%-Lw%?%{bw}%n*%f%t%?(%u)%?%{wk}%?%+Lw%?"

tmux -t ipython sh -c 'while true; do python mngmt_console.py ; clear; done'
tmux -t r1 sh -c 'while true; do telnet 127.0.0.1 60101 ; echo Retrying in 1 secods...; sleep 1 ; clear; done'
tmux -t r2 sh -c 'while true; do telnet 127.0.0.1 60102 ; echo Retrying in 1 secods...; sleep 1 ; clear; done'
tmux -t r3 sh -c 'while true; do telnet 127.0.0.1 60103 ; echo Retrying in 1 secods...; sleep 1 ; clear; done'
tmux -t sw1 sh -c 'while true; do telnet 127.0.0.1 60201 ; echo Retrying in 1 secods...; sleep 1 ; clear; done'
select 1


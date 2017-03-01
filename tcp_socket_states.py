#!/usr/bin/env python
import sys
'''
http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=include/net/tcp_states.h;hb=HEAD
    TCP_ESTABLISHED,
    TCP_SYN_SENT,
    TCP_SYN_RECV,
    TCP_FIN_WAIT1,
    TCP_FIN_WAIT2,
    TCP_TIME_WAIT,
    TCP_CLOSE,
    TCP_CLOSE_WAIT,
    TCP_LAST_ACK,
    TCP_LISTEN,
    TCP_CLOSING
'''
str_arr = [
    "established",
    "syn_sent",
    "syn_recv",
    "fin_wait1",
    "fin_wait2",
    "time_wait",
    "close",
    "close_wait",
    "last_ack",
    "listen",
    "closing"
]

TCP_STAT_FILE = "/proc/net/tcp"

def print_stats(stats):
    sys.stdout.write('{')
    s=','.join(
        map(lambda x,y: '"system.net.tcp.state.%s": %d' % (x,y), str_arr, stats)
    )
    sys.stdout.write(s)
    sys.stdout.write('}\n')

if __name__ == '__main__':
    f = open(TCP_STAT_FILE, 'r')
    if not f:
        sys.exit(1)
    # init stats array
    size = len(str_arr)
    stats = [0 for i in xrange(size)]
    # skip first line
    f.readline()
    for line in f:
        fields = line.split()
        idx = -1
        try:
            idx = int(fields[3], 16) - 1
        except:
            continue
        if idx < 0 or idx >= size:
            # value out of bound, skip it
            continue
        stats[idx] += 1
    print_stats(stats)
    f.close()
    sys.exit(0)

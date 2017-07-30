from mininet.topo import *
from mininet.topolib import *
from mininet.node import *
from mininet.link import TCLink
from mininet.net import Mininet
from optparse import OptionParser
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import Intf

import os
import sys
import time

class MyTreeTopo( Topo ):
    "Topology for a tree network with a given depth and fanout."

    def build( self, depth=1, fanout=2 ):
        self.hostNum = 1
        self.switchNum = 1
        self.addTree( depth, fanout )

    def addTree( self, depth, fanout ):
        isSwitch = depth > 0
        if isSwitch:
            node = self.addSwitch( 's%s' % self.switchNum )
            self.switchNum += 1
            for _ in range( fanout ):
                child = self.addTree( depth - 1, fanout )
                self.addLink( node, child, bw=100, max_queue_size=1000)
        else:
            node = self.addHost( 'h%s' % self.hostNum )
            self.hostNum += 1
        return node

def simpleTest(ip):
    depth = 1
    topo = MyTreeTopo(depth = 3, fanout = 2)
    net = Mininet(topo=topo, switch=OVSSwitch,
        controller=lambda name: RemoteController(name, ip=ip),
        autoSetMacs=True, link=TCLink)
    # add interface
    hosts = net.hosts
    switches = net.switches
    h1 = hosts[0]
    h2 = hosts[1]
    h3 = hosts[2]
    h4 = hosts[3]
    h6 = hosts[5]

    Link(h1, net.switches[2], intfName1='h1-eth1')
    h1.cmd('ifconfig h1-eth1 down')
    h1.cmd('ifconfig h1-eth1 hw ether 00:00:00:00:00:11')
    h1.cmd('ifconfig h1-eth1 up')
    h1.cmd('ifconfig h1-eth1 10.0.0.11 netmask 255.255.255.0')

    Link(h3, net.switches[3], intfName1='h3-eth1')
    h3.cmd('ifconfig h3-eth1 down')
    h3.cmd('ifconfig h3-eth1 hw ether 00:00:00:00:00:13')
    h3.cmd('ifconfig h3-eth1 up')
    h3.cmd('ifconfig h3-eth1 10.0.0.13 netmask 255.255.255.0')

    net.start()
    os.system('./limit.sh')
    # traffic generate
    h1.cmd('./normal.sh h1 400 &')
    pid1 = int(h1.cmd('echo $!'))

    h3.cmd('./normal.sh h3 400 &')
    pid3 = int(h3.cmd('echo $!'))

    h2.cmd('python attack.py 2000 100 0.001 > cache/t1 &')
    pid2 = int(h2.cmd('echo $!'))
    h4.cmd('python attack.py 2000 100 0.001 > cache/t2 &')
    pid4 = int(h4.cmd('echo $!'))
    h6.cmd('python attack.py 2000 100 0.001 > cache/t3 &')
    pid6 = int(h6.cmd('echo $!'))

    # CLI
    CLI(net)
    h1.cmd('kill -9 ', pid1)
    h2.cmd('kill -9 ', pid2)
    h3.cmd('kill -9 ', pid3)
    h4.cmd('kill -9 ', pid4)
    h6.cmd('kill -9 ', pid6)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simpleTest(sys.argv[1])
00
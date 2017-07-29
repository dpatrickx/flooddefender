if [ $1 = "h1" ]; then
    tcpreplay --pps=$2 --loop=100 --intf1=$1-eth0 --intf2=$1-eth1 --cachefile data/in5.cach data/out5.pcap
elif [ $1 = "h2" ]; then
    tcpreplay --pps=$2 --loop=100 --intf1=$1-eth0 --intf2=$1-eth1 --cachefile data/in6.cach data/out6.pcap
elif [ $1 = "h3" ]; then
    tcpreplay --pps=$2 --loop=100 --intf1=$1-eth0 --intf2=$1-eth1 --cachefile data/in2.cach data/out2.pcap
fi

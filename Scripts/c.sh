s=`ovs-ofctl -O OpenFlow14 dump-flows s1 | grep cookie | awk 'END{print NR}'`
s1=`ovs-ofctl -O OpenFlow14 dump-flows s1 | grep "nw_src=10.0.0.1," | awk 'END{print NR}'`
s11=`ovs-ofctl -O OpenFlow14 dump-flows s1 | grep "nw_src=10.0.0.11," | awk 'END{print NR}'`
s2=`ovs-ofctl -O OpenFlow14 dump-flows s1 | grep "nw_src=10.0.0.2," | awk 'END{print NR}'`
s12=`ovs-ofctl -O OpenFlow14 dump-flows s1 | grep "nw_src=10.0.0.12," | awk 'END{print NR}'`
s3=`ovs-ofctl -O OpenFlow14 dump-flows s1 | grep "nw_src=10.0.0.3," | awk 'END{print NR}'`
s4=`ovs-ofctl -O OpenFlow14 dump-flows s1 | grep "nw_src=10.0.0.4," | awk 'END{print NR}'`

echo $s1" "$s11" "$s2" "$s12" "$s3" "$s4" "$s
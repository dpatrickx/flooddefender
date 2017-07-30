flowLimit=1000

sudo ovs-vsctl set bridge s1 protocols=OpenFlow14
sudo ovs-vsctl set bridge s2 protocols=OpenFlow14
sudo ovs-vsctl set bridge s3 protocols=OpenFlow14
sudo ovs-vsctl set bridge s4 protocols=OpenFlow14
sudo ovs-vsctl set bridge s5 protocols=OpenFlow14
sudo ovs-vsctl set bridge s6 protocols=OpenFlow14
sudo ovs-vsctl set bridge s7 protocols=OpenFlow14

sudo ovs-vsctl -- --id=@s30 create Flow_Table flow_limit=$flowLimit overflow_policy=evict -- set Bridge s3 flow_tables:0=@s30
sudo ovs-vsctl -- --id=@s31 create Flow_Table flow_limit=$flowLimit overflow_policy=evict -- set Bridge s3 flow_tables:1=@s31

sudo ovs-vsctl -- --id=@s40 create Flow_Table flow_limit=$flowLimit overflow_policy=evict -- set Bridge s4 flow_tables:0=@s40
sudo ovs-vsctl -- --id=@s41 create Flow_Table flow_limit=$flowLimit overflow_policy=evict -- set Bridge s4 flow_tables:1=@s41

sudo ovs-vsctl -- --id=@s60 create Flow_Table flow_limit=$flowLimit overflow_policy=evict -- set Bridge s6 flow_tables:0=@s60
sudo ovs-vsctl -- --id=@s61 create Flow_Table flow_limit=$flowLimit overflow_policy=evict -- set Bridge s6 flow_tables:1=@s61

sudo ovs-vsctl -- --id=@s1 create Flow_Table flow_limit=2000 overflow_policy=evict -- set Bridge s1 flow_tables:1=@s1
sudo ovs-vsctl -- --id=@s2 create Flow_Table flow_limit=2000 overflow_policy=evict -- set Bridge s2 flow_tables:1=@s2
sudo ovs-vsctl -- --id=@s5 create Flow_Table flow_limit=2000 overflow_policy=evict -- set Bridge s5 flow_tables:1=@s5
sudo ovs-vsctl -- --id=@s7 create Flow_Table flow_limit=2000 overflow_policy=evict -- set Bridge s7 flow_tables:1=@s7

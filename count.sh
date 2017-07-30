cat $1 | grep "###### PACKET_REMOVED - 10.0.0.1;" > normal
cat $1 | grep "###### PACKET_REMOVED - 10.0.0.11;" >> normal
cat $1 | grep "###### PACKET_REMOVED - 10.0.0.2;" >> normal
cat $1 | grep "###### PACKET_REMOVED - 10.0.0.12;" >> normal

sort normal > temp
cat temp | awk -F . '{print $1}' > normal

b=`head -1 normal`
e=`tail -1 normal`
be=`date -d "$b" +%s`
en=`date -d "$e" +%s`

num=$(( $en-$be ))

allFlowRemoved=`cat normal | awk 'END{print NR}'`

python compute.py $allFlowRemoved $num
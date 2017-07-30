cat $1 | grep "###### MESSAGE" | awk -F . '{print $1}' | sort > temp
b=`head -1 temp`
e=`tail -1 temp`
echo $b" "$e
be=`date -d "$b" +%s`
en=`date -d "$e" +%s`

i=$be
while [ "$i" -le "$en" ]; do
    t=`date -d @"$i"  "+%Y-%m-%d %H:%M:%S"`
    # t=`date -d @"$i"  "+%H:%M:%S"`
    num=`cat $1 | grep "$t" | awk 'END{print NR}'`
    echo $num
    i=$(($i+1))
done

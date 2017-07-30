cat $1 | grep "###### MESSAGE" | awk -F . '{print $1}' | sort > temp
b=`head -1 temp`
e=`tail -1 temp`
be=`date -d "$b" +%s`
en=`date -d "$e" +%s`

echo $((  en - be ))

> $1
for (( i = 0; i <= 100000; i++ )); do
    ./c.sh >> $1
    sleep 1s
done
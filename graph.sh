#!/bin/sh

rm output1
rm output2
python3 $1 &
testpid=$!
sudo ./wss.pl -C $testpid 0.01 > output1 &
pid=$!
sleep $2
sudo kill $pid
sudo kill $testpid
# python3 graph.py


# python3 test.py &
# testpid=$!
python3 $1 &
testpid=$!
i=
while [ $((i+=1)) -le $2 ]
do
	sudo ./wss.pl -C -d 1 $testpid 0.1 >> output2	
	# pid=$!
	# # sleep 1
	# sudo kill $pid
done
sudo kill $testpid
python3 graph.py
python3 tests/test.py &

adb shell top -b -d 10 -n 3 | grep com.mgmresorts > memory.log 
sleep 10
processId=$(ps -ef | grep 'ABCD' | grep -v 'adb' | awk '{ printf $2 }')
kill -9 processId

adb logcat | grep http > network.log & sleep 10 & processId1=$(ps -ef | grep 'ABCD' | grep -v 'adb' | awk '{ printf $2 }') & kill -9 processId1



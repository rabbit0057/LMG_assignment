python3 tests/test.py &
sleep 20
adb logcat | grep http > network.log & sleep 10 & processId1=$(ps -ef | grep 'ABCD' | grep -v 'adb' | awk '{ printf $2 }') & kill -9 processId1



# a file that deletes all songs from the songs tab in the library section

while [ 1 ]
do
    adb shell input swipe 392 632 392 632 500
    sleep 1
    adb shell input tap 529 1146
    sleep 1
    adb shell input tap 777 1306
    sleep 1
done
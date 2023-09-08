song=$(python main.py -i 0)
count=1

while [ "$song" != "done" ]
do
    echo $song
    adb shell input tap 987 2188 # click search in bottom right
    sleep 1
    adb shell input tap 423 260 # click the search box
    sleep 1 # wait for menu to load
    adb shell input tap 956 275 # clear the search box of a song
    sleep 1
    adb shell input text \"$song\"  # searches for the song
    sleep 1
    adb shell input keyevent 66 # presses enter on the keyboard

    sleep 3 # wait for search to finish
    adb shell input swipe 561 546 561 546 500 # holds the song down for the playlist add popup for 500ms
    sleep 1
    adb exec-out screencap -p > temp_cap.png
    sleep 1
    add_to_playlist_coords=$(python tesser.py)
    adb shell input tap $add_to_playlist_coords
    sleep 1
    adb shell input tap 234 504 # select playlist to add to
    sleep 1

    count=$((count+1))
    song=$(python main.py -i $count)
done
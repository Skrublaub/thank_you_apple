# Overview

I needed a good way to transfer a playlist from ViMusic to Apple Music. The apple
API costs $100/year to access which is too much. I automated the process
of transferring songs in the next best way, automatically clicking the songs
and adding them to a playlist.

This uses google's tesseract to analyze a Pixel 7a screenshot to find the add
to playlist button. I did this because the add to playlist button could appear in two different
locations which is a huge pain to deal with. Text recognition is the solution.

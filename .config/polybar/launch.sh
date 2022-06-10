#!/bin/bash

killall -q polybar

while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

polybar left &
polybar mid &
polybar right &
#polybar mpd & # uncomment this line (and modify bar/mpd in config.ini) if you have a second monitor 

echo "meow? (waiting for something to happen?)"

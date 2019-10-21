#!/usr/bin/env bash
#Title......: resizeME.sh
#Description: a simple diet that gets your pics slim and beautiful, ready for the web
#Author.....: GABA
#Version....: 0.1a
#Usage......: bash resizeME.sh

if command -v convert >/dev/null 2>&1 ; then
    echo "ImageMagick found! $(convert -version | head -n 1)"
else
    echo "ImageMagick not found"
fi
if command -v exiftool >/dev/null 2>&1 ; then
    echo "exiftool found! Version: $(exiftool -ver)"
else
    echo "exiftool not found"
fi

# get current folder
FOLDER=$PWD
# max height
WIDTH=1024
# max width
HEIGHT=768

#resize jpg only to either height or width, keeps proportions using imagemagick
find ${FOLDER} -iname '*.jpg' -exec convert \{} -verbose -resize $WIDTHx$HEIGHT\> \{} \;
#strip EXIF data for output jpg
for i in *.jpg; do echo "Processing $i"; exiftool -all= "$i"; done

#else
#	echo "Dependencies are not met! Install $1 and 2$ first, then re-run this program."
#fi

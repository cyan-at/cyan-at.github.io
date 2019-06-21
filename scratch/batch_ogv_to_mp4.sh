#!/bin/bash

# usage: ./batch_ogv_to_mp4.sh on a system with ffmpeg installed, .sh must be *in* directory with ogv files

# or put this in your bash:
# ffmpeg_ogv_to_mp4() {
#     if [ "$#" -gt 0 ]
#     then
#         f=$1
#         if [ -e "$1" ]; then
#             mp4="${f//ogv/mp4}"
#             echo "File exists converting to $mp4"
#             ffmpeg -i $1 -c:v libx264 -preset veryslow -crf 22 -c:a aac -b:a 160k -strict -2 $mp4
#         else 
#             echo "File does not exist"
#         fi 
        
#     fi
# }
# alias ffmp4=ffmpeg_ogv_to_mp4

files=$(ls -d -1 $PWD/** | grep .ogv)

foo=() # add all arguments to an array
for var in $files
do
  echo $var
  foo+=("$var")

  var2=${var//ogv/mp4}
  echo $var2

  if test -f "$var2"; then
    echo "skipping $var2"
  else
    # 1. convert to mp4
    ffmpeg -i $var \
      -c:v libx264 -preset veryslow -crf 22 \
      -c:a aac -b:a 160k -strict -2 \
      $var2

    # 2. delete ogv
    rm $var
  fi
done

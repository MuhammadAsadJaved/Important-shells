for i in *.mp3;
  do name=`echo "$i" | cut -d'.' -f1`
  echo "$name"
  ffmpeg -i "$i" -f s16le -ar 16000 -ac 1 -acodec pcm_s16le  "${name}.pcm"
done

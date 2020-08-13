#This shell will convert all videos in a directory to images, Note: Please run this shell inside the directory that include vidoes
for f in *.mp4; 
do 
  echo Processing $f ; 
  ffmpeg -i $f -vf fps=1/600 $f%04d.jpg  #where FPS 1/600 means 1 frame after every 600 seconds (10 minutes)
done;

# Check if FFMPEG is installed
YTDL=youtube-dl
command -v $YTDL >/dev/null 2>&1 || {
	echo >&2 "This script requires youtube-dl. Aborting."; exit 1;
}

# Check number of arguments
if [ "$#" -lt 2 ]; then
	echo "Usage: sh downloadvideos.sh <number-of-videos> <category-name>"
	exit 1
fi

txt=".txt"
name="$2"

if [ "$(uname)" == "Darwin" ]; then
    # Mac OS X platform
    mid=$(grep -E "\t$name \(" youtube8mcategories.txt | grep -o "\".*\"" | sed -n 's/"\(.*\)"/\1/p')
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # GNU/Linux platform
    mid=$(grep -E "\t$name \(" youtube8mcategories.txt | grep -o "\".*\"" | sed -n 's/"\(.*\)"/\1/p')
fi
mid=$mid$txt

mkdir -p videos

if [ "$1" -eq 0 ]; then
	while read line
		do
			$YTDL -f 18 "http://www.youtube.com/watch?v=$line" -o ./videos/"$name%(title)s-%(id)s-360p.%(ext)s"
			$YTDL -f 22 "http://www.youtube.com/watch?v=$line" -o ./videos/"$name%(title)s-%(id)s-720p.%(ext)s"
		done < category-ids/$mid
else
	limit=$1
	rm -rf log.txt
	while read line
		do
			if [ "$limit" -gt 0 ]; then
				limit=$(($limit-1))
				#$YTDL -f 22 "http://www.youtube.com/watch?v=$line" -o /videos/"$name%(title)s-%(id)s-720p.%(ext)s" 2>&1 | tee log.txt
				$YTDL -f 18 "http://www.youtube.com/watch?v=$line" -o /videos/"$name%(title)s-%(id)s-360p.%(ext)s" 2>&1 | tee -a log.txt
				error=$(grep -c ERROR log.txt)
				if [ "$error" -gt 0 ]; then
					limit=$(($limit+1))
				fi
				rm -rf log.txt
			else
				break
			fi
		done < category-ids/$mid
fi
# Check number of arguments
if [ "$#" != "1" ]; then
	echo "Usage: sh downloadmulticategoryvideos.sh <selected-category-file-name>"
	exit 1
fi

while read line
	do
		set -- $line
		sh downloadcategoryids.sh $1
		sh downloadvideos.sh $2 $1
	done < "$1"
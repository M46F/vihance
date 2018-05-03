.PHONY: all

all: build download

build:
	docker build -t vihance/scraper -f Dockerfile .

download:
	 docker run -v ~/videos:/videos -it vihance/scraper /bin/sh -c "cd downloader && sh downloadmulticategoryvideos.sh selectedCategories.txt"

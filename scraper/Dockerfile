FROM python:2.7-alpine3.7

RUN apk update && apk add ca-certificates && apk add openssl

ADD /utils /downloader
ADD /selectedCategories.txt /downloader/selectedCategories.txt

RUN wget https://storage.googleapis.com/pub/gsutil.tar.gz && tar xfz gsutil.tar.gz
ENV PATH="${PATH}:/gsutil"

RUN wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl && chmod a+rx /usr/local/bin/youtube-dl
### Dependencies

- Docker

### Usage

- modify selectedCategories with following format
```
<Category> <Num video to scrape>

Ex:
Car 10
Gaming 100
```
- call `make`, it will download the youtube videos(720p and 360p version for each video) in docker container and bindmount it into your `~/videos` directory
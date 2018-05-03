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
- call `make`, it will download the youtube video in docker container and bindmount it into your `~/videos` directory
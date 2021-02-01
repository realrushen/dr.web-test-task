## Getting Started

This instructions will help setting up this project locally.
To get a local copy up and running follow this simple steps.

### Prerequisites

You need [python 3.8](https://www.python.org/downloads/), [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) to run this project

### Installation

1. Clone the repo
   ```shell script
   git clone https://github.com/realrushen/dw-test-task.git
   ```
2. You can configure project settings in **.env.dev** for development build and **.env.prod, .env.prod.db** for production build. 
   By default `FRESH_START=1` env variable is set to flush db, make migrations and collect static files on startup.
   Feel free to remove it, if you want.
   
3. Run docker-compose.prod.yaml for production build with nginx, gunicorn, PostgresSQL
   ```shell script
   docker-compose -f docker-compose.prod.yml up -d --build 
   ```
   or run docker-compose.yaml for development build with default django dev server and PostgreSQL
   ```shell script
   docker-compose up -d --build
   ```

## Usage

#### Upload file endpoint
```shell script
curl --location --request POST 'http://localhost:8080/storage/' \
--form 'file=@"/home/username/path/to/file"'
```
Maximum file size to upload in prod build is 100Mb. 

#### Download file endpoint
```shell script
curl --location --output - --request GET 'http://localhost:8080/storage/<hash>/'
```

#### Delete file endpoint
```shell script
curl --location --request DELETE 'http://localhost:8080/storage/<hash>/'
```

## License
Distributed under the MIT License.

## Contact
Aleksandr Karakchiev - realrushen@gmail.com




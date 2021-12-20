<img align="right" width="200" height="200" src="./docs/luigi.gif" alt="luigi.gif">

# Luigi

Luigi is a sample application that uses the [GitHub API](https://api.github.com/search/code) to search for vs code extensions.
It sports a web dashboard built with React.js, a backend api built in Flask, a database powered with sqlite and uses redis for caching.

## Requirements

- Python 3.9+
- SQLite 3
- Redis

Additional requirements:

- Docker v20.10.11
- Docker compose v1.28.5

## Getting started

First you need some environment variables in place to run the application.
All the variables are stored in `.env.example` file.

```bash
λ cp .env.example .env
```

The easiest way to spin up everything is to run the following command:

```bash
λ docker-compose up
```

This will build the containers from the Dockerfiles, setup the database, launch
redis and start both the flask api and react dashboard containers.

### Terminal life:

If you don't want to use docker-compose, you can run the applications separately on your terminal.

### Flask api

All our flask api is in the `api` folder. So make sure you are in the right directory. (`cd api`)
Then run the following commands.

1. Install all the required dependencies in a virtual environment which are
   present in the requirements.txt file and pipenv file.

   ```bash
   λ pip install -r requirement.txt
   ```

   or if you are using pipenv, you can run `pipenv install` to install them.

   ```bash
   λ pipenv install
   ```

   Now would be a good time to switch to the virtual environment.

2. Launch the init script.

   The init script will create the database, the tables and will also launch the flask server.

   ```bash
   λ sh init.sh
   ```

   Or you can execute each step manually.

   - Setup the database

   ```bash
   λ python db.py
   ```

   - Start the server

   We can start the server using gunicorn

   ```bash
   λ gunicorn app:'create_app()' -b:5000
   ```

   Or we can start the server directly from the file.

   ```bash
   λ python app.py
   ```

   You can easily control the `APP_PORT` environment variable to change the port.
   But if you're using default port, the server will be available at `localhost:5000`.

3. Launch redis

   The flask api uses redis for caching which is a good way to speed up the
   application and cache any subsequent request from the same user for a given
   time. This ability is given to the flask server by the
   [`flask_caching`](https://flask-caching.readthedocs.io/en/latest/) package.

   If you have redis installed locally, you can launch it using the following command.

   ```bash
   λ redis-server
   ```

   > If you're using the above command, you'll have to change the `CACHE_REDIS_URL=redis://redis:6379/0` to `CACHE_REDIS_URL=redis://localhost:6379/0`

   Or, if you have the redis docker image available, you can launch it using the
   following command.

   ```bash
   λ docker run -d -p 6379:6379 --name redis redis
   ```

   Or, using docker-compose you can launch it using the following command.

   ```bash
   λ docker-compose up redis
   ```

### React dashboard

The react dashboard is built using create-react-app and uses
[`react-scripts`](https://www.npmjs.com/package/react-scripts) to run and build
the application.

1. Install the dependencies.

   ```bash
   λ npm install
   ```

2. Run the application.

   ```bash
   λ npm start
   ```

   This will launch a local server on port `8000` or whatever port is set via the
   environment variable `PORT`.

**Please ensure your environment variables are set up correctly.**

> Note:
> To load environment variables if you're a terminal person, you might want > to
> use [direnv](https://direnv.net/). Simply, make the variables present in
> `.env.example` available by exporting them in a `.envrc` file.

## Prebuilt containers

Following are the steps to build the containers from the Dockerfiles:

- Flask api

  ```bash
  λ docker build --build-arg DATABASE_URL=database.db -t luigi_api -f Dockerfile.api .
  ```

  NOTE: It can accept a custom database url as per the user choice otherwise it
  will use create a default database.db file. This can come handy if you wish to
  mount the database to a volume.

- React dashboard

  ```bash
  λ docker build -t luigi_client -f Dockerfile.client .
  ```

  This builds a production react app and serves it via nginx.

## Architecture

- The backend is written in python with [Flask](https://pypi.org/project/Flask/)
  which releases a RESTful api.
- The frontend is written in typescript and uses
  [React.js](https://pypi.org/project/Flask/) that interacts with the rest
  api.
- [Sqlite3](https://www.sqlite.org/index.html) is being used as the
  SQL database of choice.
- [Redis](https://www.sqlite.org/index.html) provides the caching layer.
- All operations are possible via the RESTful api
- The whole project is production ready and uses docker and docker-compose to
  run the containers. _(p.s. You might want to switch the database if you are planning to push this to production)_

## Contribution

Well this is kind of a learning project, feel free to fork it and happy hacking :)

## License

[MIT License](http://mit-license.org/)

Copyright © 2021 Shashank Srivastav

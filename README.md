
This program is a web based sudoku game.
It runs in python 3.9, with django, and a postgresql database.
it expects a database named sudoku hosted on localhost, port 5432
the database username and password are expected to be 'postgres'

Set up the database : 

```
sudo -u postgres psql

postgres=# CREATE DATABASE sudoku;
```

Install dependencies : 

```
make install-virtualenv
```

Run migrations :

```
make migrate
```

Run tests :

```
make test
```

Locally run server :

```
make run-server
```

You can access the sudoku pages at [http://127.0.0.1:8000/sudoku/]

The UX is definitely not perfect, you don't always have feedback on your actions, but it is functional.


This program runs in python 3.9, with a postgresql database.
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


This program is a web based sudoku game.
It is fully dockerized, you will need docker and docker-compose installed
It runs in python 3.9, with django, and a postgresql database.

A Makefile hosts a few useful commands

Run migrations :

```
make migrate
```

Run tests :

```
make test
```

Run coverage :

```
make coverage
```

Locally run server :

```
make run-server
```

You can access the sudoku pages at [http://127.0.0.1:8000/sudoku/]

The UX is definitely not perfect, you don't always have feedback on your actions, but it is functional.

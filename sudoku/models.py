from django.db import models

from django.contrib.postgres.fields import ArrayField

def empty_grid():
    return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

class Sudoku(models.Model):
    grid = ArrayField(
                ArrayField(
                    models.IntegerField(blank=True),
                    size=9
                ),
                size=9,
                default=empty_grid
            )

    def possible_number(self, rind, cind):
        for number in range(1, 10):
            if number not in self.limiting_cases(rind, cind):
                yield number

    def limiting_cases(self, rind, cind):
        yield from self.row(rind)
        yield from self.col(cind)
        yield from self.square(rind, cind)

    def row(self, rind):
        yield from self.grid[rind]

    def col(self, cind):
        yield from list(zip(*self.grid))[cind]

    def square(self, rind, cind):
        rowrange = range(3*(rind//3), 3*(rind//3)+3)
        colrange = range(3*(cind//3), 3*(cind//3)+3)
        for x in rowrange:
            for y in colrange:
                yield self.grid[x][y]


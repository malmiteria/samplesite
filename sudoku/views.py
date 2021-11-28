from django.shortcuts import render
from sudoku.models import Sudoku

def index(request):
    return render(request, 'sudoku/index.html', {'grid': Sudoku.objects.create()})

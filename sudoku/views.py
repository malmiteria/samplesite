from django.shortcuts import render
from sudoku.models import Sudoku
from sudoku.forms import SudokuCreateForm, SudokuEditForm

def index(request):
    return render(request, 'sudoku/index.html', {'grids': Sudoku.objects.all()})

def create_view(request):
    form = SudokuCreateForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form':form}

    return render(request, 'sudoku/create_view.html', context)

def edit_grid(request, grid_id):
    sudoku = Sudoku.objects.get(pk=grid_id)
    form = SudokuEditForm(request.POST or None)
    if request.POST:
        sudoku.grid = form.get_grid_from_inputs()
        sudoku.save()
    context = {
        'form':form,
        'grid': sudoku
    }
    return render(request, 'sudoku/edit_grid.html', context)

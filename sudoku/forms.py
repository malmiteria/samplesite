from django import forms
from .models import Sudoku


class SudokuCreateForm(forms.ModelForm):

    class Meta:
        model = Sudoku
        fields = []


class SudokuEditForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(9):
            for j in range(9):
                self.fields[f'cell({i}, {j})'] =  forms.IntegerField(required=False)

    def get_grid_from_inputs(self):
        return list(self.get_rows_from_inputs())
    
    def get_rows_from_inputs(self):
        row = []
        for value in self.get_value_from_inputs():
            row.append(value)
            if len(row) == 9:
                yield row
                row = []
    
    def get_value_from_inputs(self):
        for field in self.fields:
            try:
                yield int(self.data[field])
            except ValueError:
                yield 0


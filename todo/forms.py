from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "memo", "important"] # fields = "__all__" means that all fields will be included


from django import forms
from .models import Note
from ckeditor.widgets import CKEditorWidget

class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Note
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control input-lg'
            }),
        }
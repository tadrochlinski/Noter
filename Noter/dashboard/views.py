from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import NoteForm
from .models import Note
import uuid


@login_required
def dashboard(request):
    user = request.user
    notes = Note.objects.filter(user=user)
    context = {'user_logged_in': True, 'user': user, 'notes': notes}

    return render(request, 'dashboard/dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('landing_page')

@login_required   
def create_note(request, slug=None):
    if slug:
        note = get_object_or_404(Note, slug=slug)
    else:
        note = None

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        form_class = NoteForm
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            if not note.slug:
                note.slug = slugify(note.title)
                while Note.objects.filter(slug=note.slug).exists():
                    note.slug = slugify(note.title) + str(uuid.uuid4())[:8]
            note.save()
            return redirect('dashboard') 
    else:
        form = NoteForm(instance=note)

    context = {'form': form}

    return render(request, 'dashboard/create_note.html', context)

def view_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    return render(request, 'dashboard/note.html', {'note': note})

def edit_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('view_note', slug=note.slug) 
    else:
        form = NoteForm(instance=note)

    return render(request, 'dashboard/edit_note.html', {'form': form, 'note': note})

def delete_note(request,slug):
    note = get_object_or_404(Note, slug=slug)
    if request.method == 'POST':
        note.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_note.html', {'note': note})
    



from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .models import Notes

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})

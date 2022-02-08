from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from notes.serializers import NoteSerializer
from notes.models import Note

# Create your views here.
class ListNoteAPIView(ListAPIView):
    """This endpoint list all of the available notes from the database"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class CreateNoteAPIView(CreateAPIView):
    """This endpoint allows for creation of a note"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UpdateNoteAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific note by passing in the id of the note to update"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class DeleteNoteAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Note from the database"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
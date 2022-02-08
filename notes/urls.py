from django.urls import path
from notes import views

urlpatterns = [
    path("",views.ListNoteAPIView.as_view(),name="note_list"),
    path("create/", views.CreateNoteAPIView.as_view(),name="note_create"),
    path("update/<int:pk>/",views.UpdateNoteAPIView.as_view(),name="update_note"),
    path("delete/<int:pk>/",views.DeleteNoteAPIView.as_view(),name="delete_note")
]
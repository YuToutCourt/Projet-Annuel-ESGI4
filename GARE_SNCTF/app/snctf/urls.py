from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/trains", views.get_all_trains, name="get_all_trains"),
    path("api/train", views.get_train_by_uuid, name="get_train_by_uuid"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("boards/", views.boards, name="boards"),
    path("board/", views.board_detail, name="board_detail"),
]
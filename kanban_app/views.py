from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class DashboardView(TemplateView):
    template_name = "pages/dashboard/index.html"

class BoardsView(TemplateView):
    template_name = "pages/boards/index.html"

class BoardDetailView(TemplateView):
    template_name = "pages/board/index.html"



def index(request):
    return render(request, IndexView.template_name)

def dashboard(request):
    return render(request, DashboardView.template_name)

def boards(request):
    return render(request, BoardsView.template_name)

def board_detail(request):
    board_id = request.GET.get("id")  
    return render(request, BoardDetailView.template_name, {"board_id": board_id})

# def tasks_list_create(request):
#     return render(request, BoardDetailView.template_name)
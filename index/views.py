from django.shortcuts import render

# Create your views here.
def index(request):
        return render(request, 'index.html')

def category_grid(request):
        return render(request, 'categories-grid.html')

def category_list(request):
        return render(request, 'categories-list.html')

def category_single(request):
        return render(request, 'single-post.html')
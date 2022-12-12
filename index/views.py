from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, render, redirect
from account.models import *
from django.views.generic import *
from .forms import *
# Create your views here.

def index(request):
        objs = Post.objects.all().order_by('-created_on')
        CAT1 = Post.objects.filter(category__name = "Desserts").order_by('-created_on')
        CAT2 = Post.objects.filter(category__name = "Recipes").order_by('-created_on')
        CAT3 = Post.objects.filter(category__name = "Vegan").order_by('-created_on')
        CAT4 = Post.objects.filter(category__name = "Dinner").order_by('-created_on')
        categories = Category.objects.all()
        def get_context_data(self, **kwargs):
            context = super(index, self).get_context_data(**kwargs)
            context["categories"] = categories
            return context
        
        list = {
                'categories': categories,
                'objs': objs,
                'CAT1': CAT1,
                'CAT2': CAT2,
                'CAT3': CAT3,
                'CAT4': CAT4
        
        }
        return render(request, 'index.html', list)
        
def Add_PostView(request):
        if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                #print(form.data)
                # initial= {
                #         "author": request.user,
                #         "title":request.POST["title"],
                #         "content":request.POST["content"],
                # }
                # form['author'] = Post.objects.get(pk = request.user.id)
                if form.is_valid():
                        ab = form.save(commit = False)
                        ab.author = request.user
                        ab.save()
                        return redirect('index')
        else:
            form = PostForm()
            return render(request, 'add_post.html', {'form': form})
def category_grid(request,categ=None):
        if categ:
                print(categ)
                objs = Post.objects.filter(category__name = categ).order_by('-created_on')
        else:
                objs = Post.objects.all().order_by('-created_on')
        return render(request, 'categories-grid.html', {'objs': objs, 'categ': categ})

def category_list(request, categ = None):
        if categ:
                objs = Post.objects.filter(category__name = categ).order_by('-created_on')
        else:
                objs = Post.objects.all().order_by('-created_on')
        return render(request, 'categories-list.html', {'objs': objs,'categ': categ, 'list':list})

class category_single(DetailView):
        model = Post
        template_name = 'single-post.html'
        def slugg (request, slug):
                obj = Post.objects.get(slug=slug)
                return render(request,'single-post.html', {'obj': obj})
def about(request):
        return render(request, 'about.html')

def contact(request):
        return render(request, 'contact.html')

# def AuthorView(request):
        #         objs = Post.objects.all()
        #         return render(request, 'author_chamber.html', { 'objs': objs } ) 
        #         # model = Post
        #         # template_name = 'author_chamber.html'
        #         #  all_objs
        #         # def get_context_data(self):
        #                 # if  self.request.user.is_author:

#         # ...